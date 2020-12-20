from collections import defaultdict
import logging


class GameConsole:

    def __init__(self, raw_mem=None):

        if raw_mem is None:
            raw_mem = []

        logging.debug(f'Creating new game console from memory input.')

        self.accumulator = 0
        self.ip = 0
        self.prgm = defaultdict(tuple)
        self.stopped = False
        self.visited_ip = set()

        for ipcount, line in enumerate(raw_mem):
            instruction = line.strip('\n').split()
            operation = instruction[0]
            argument = int(instruction[1])
            self.prgm[ipcount] = (operation, argument)

        self.last_instr = len(self.prgm)

    # classmethod to generate an instance from a filename instead of memory input
    # this is for convenience really...
    @classmethod
    def from_file(cls, f_name):
        with open(f_name, 'r') as f:
            mem = [x.strip('\n') for x in f.readlines()]
            return cls(mem)

    def run(self):
        # run until we meet an endless loop and set the stopped flag
        while not self.stopped:
            # check if the program terminated properly by trying to execute an instruction exactly below the last
            if self.ip == self.last_instr + 1:
                logging.info(f'[{self.ip}, {self.accumulator}]: Program terminated.')
                self.stopped = True

            # check if we have been at the IP before
            elif self.ip not in self.visited_ip:
                # add IP to already visited list so we don't go here again.
                self.visited_ip.add(self.ip)

                # get the next instruction and execute it
                op, arg = self.prgm[self.ip]
                logging.debug(f'[{self.ip}, {self.accumulator}]: {op} {arg}')
                self._exec_op(op, arg)

            # we've been here before, stop execution
            else:
                logging.info(f'[{self.ip}, {self.accumulator}]: Visited IP before, stopping.')
                self.stopped = True

    def _exec_op(self, op, arg):

        if op == 'nop':
            self.ip += 1
        elif op == 'acc':
            self.accumulator += arg
            self.ip += 1
        elif op == 'jmp':
            self.ip += arg
