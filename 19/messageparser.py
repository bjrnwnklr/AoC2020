from ply import lex, yacc
import messagelex

tokens = messagelex.tokens


def p_r42(p):
    """42 : 16 112
        | 89 39"""
    pass


def p_r120(p):
    """120 : 89 40
        | 16 109"""
    pass


def p_r30(p):
    """30 : 40 16
        | 26 89"""
    pass


def p_r2(p):
    """2 : 133 89
        | 137 16"""
    pass


def p_r15(p):
    """15 : 94 16
        | 92 89"""
    pass


def p_r8(p):
    """8 : 42"""
    pass


def p_r134(p):
    """134 : 40 87"""
    pass


def p_r23(p):
    """23 : 89 47
        | 16 12"""
    pass


def p_r78(p):
    """78 : 102 89
        | 26 16"""
    pass


def p_r119(p):
    """119 : 115 89
        | 5 16"""
    pass


def p_r11(p):
    """11 : 42 31"""
    pass


def p_r67(p):
    """67 : 89 63
        | 16 18"""
    pass


def p_r82(p):
    """82 : 16 40
        | 89 63"""
    pass


def p_r88(p):
    """88 : 16 16
        | 89 89"""
    pass


def p_r97(p):
    """97 : 89 110
        | 16 78"""
    pass


def p_r85(p):
    """85 : 60 16
        | 55 89"""
    pass


def p_r3(p):
    """3 : 40 16
        | 121 89"""
    pass


def p_r132(p):
    """132 : 92 16
        | 98 89"""
    pass


def p_r77(p):
    """77 : 16 97
        | 89 58"""
    pass


def p_r72(p):
    """72 : 89 16
        | 16 16"""
    pass


def p_r27(p):
    """27 : 16 99
        | 89 48"""
    pass


def p_r50(p):
    """50 : 108 89
        | 132 16"""
    pass


def p_r53(p):
    """53 : 16 45
        | 89 131"""
    pass


def p_r70(p):
    """70 : 87 87"""
    pass


def p_r36(p):
    """36 : 89 26
        | 16 63"""
    pass


def p_r65(p):
    """65 : 16 88
        | 89 100"""
    pass


def p_r38(p):
    """38 : 88 16
        | 44 89"""
    pass


def p_r25(p):
    """25 : 16 109
        | 89 63"""
    pass


def p_r81(p):
    """81 : 89 61
        | 16 3"""
    pass


def p_r136(p):
    """136 : 16 100"""
    pass


def p_r104(p):
    """104 : 92 16
        | 100 89"""
    pass


def p_r115(p):
    """115 : 26 16
        | 100 89"""
    pass


def p_r45(p):
    """45 : 16 70
        | 89 121"""
    pass


def p_r63(p):
    """63 : 16 89
        | 89 87"""
    pass


def p_r92(p):
    """92 : 16 16
        | 16 89"""
    pass


def p_r130(p):
    """130 : 89 72
        | 16 102"""
    pass


def p_r105(p):
    """105 : 118 16
        | 23 89"""
    pass


def p_r34(p):
    """34 : 16 1
        | 89 117"""
    pass


def p_r83(p):
    """83 : 67 89
        | 136 16"""
    pass


def p_r26(p):
    """26 : 89 89
        | 16 87"""
    pass


def p_r116(p):
    """116 : 16 29
        | 89 77"""
    pass


def p_r29(p):
    """29 : 68 16
        | 111 89"""
    pass


def p_r10(p):
    """10 : 89 75
        | 16 76"""
    pass


def p_r64(p):
    """64 : 16 26
        | 89 18"""
    pass


def p_r14(p):
    """14 : 89 62
        | 16 113"""
    pass


def p_r80(p):
    """80 : 89 107
        | 16 52"""
    pass


def p_r35(p):
    """35 : 16 86
        | 89 54"""
    pass


def p_r54(p):
    """54 : 81 16
        | 124 89"""
    pass


def p_r32(p):
    """32 : 66 16
        | 95 89"""
    pass


def p_r61(p):
    """61 : 98 89
        | 70 16"""
    pass


def p_r124(p):
    """124 : 120 16
        | 69 89"""
    pass


def p_r59(p):
    """59 : 100 89
        | 94 16"""
    pass


def p_r17(p):
    """17 : 89 56
        | 16 37"""
    pass


def p_r127(p):
    """127 : 16 20
        | 89 126"""
    pass


def p_r111(p):
    """111 : 16 57
        | 89 4"""
    pass


def p_r58(p):
    """58 : 33 89
        | 103 16"""
    pass


def p_r137(p):
    """137 : 89 100
        | 16 109"""
    pass


def p_r69(p):
    """69 : 88 16
        | 121 89"""
    pass


def p_r109(p):
    """109 : 89 89
        | 16 89"""
    pass


def p_r95(p):
    """95 : 89 10
        | 16 53"""
    pass


def p_r73(p):
    """73 : 16 35
        | 89 32"""
    pass


def p_r114(p):
    """114 : 94 16
        | 109 89"""
    pass


def p_r60(p):
    """60 : 38 16
        | 82 89"""
    pass


def p_r79(p):
    """79 : 63 89
        | 102 16"""
    pass


def p_r12(p):
    """12 : 89 40
        | 16 100"""
    pass


def p_r118(p):
    """118 : 16 114
        | 89 59"""
    pass


def p_r55(p):
    """55 : 16 65
        | 89 25"""
    pass


def p_r21(p):
    """21 : 16 100
        | 89 121"""
    pass


def p_r66(p):
    """66 : 89 50
        | 16 41"""
    pass


def p_r18(p):
    """18 : 16 89"""
    pass


def p_r6(p):
    """6 : 130 16
        | 101 89"""
    pass


def p_r51(p):
    """51 : 100 16
        | 94 89"""
    pass


def p_r56(p):
    """56 : 135 89
        | 79 16"""
    pass


def p_r135(p):
    """135 : 89 63
        | 16 26"""
    pass


def p_r125(p):
    """125 : 16 64
        | 89 15"""
    pass


def p_r139(p):
    """139 : 13 89
        | 17 16"""
    pass


def p_r20(p):
    """20 : 18 89
        | 44 16"""
    pass


def p_r129(p):
    """129 : 16 128
        | 89 49"""
    pass


def p_r16(p):
    """16 : B"""
    pass


def p_r62(p):
    """62 : 89 19
        | 16 7"""
    pass


def p_r5(p):
    """5 : 70 89
        | 26 16"""
    pass


def p_r24(p):
    """24 : 89 127
        | 16 80"""
    pass


def p_r107(p):
    """107 : 89 72
        | 16 121"""
    pass


def p_r108(p):
    """108 : 16 94
        | 89 98"""
    pass


def p_r102(p):
    """102 : 89 89
        | 89 16"""
    pass


def p_r1(p):
    """1 : 94 89
        | 109 16"""
    pass


def p_r19(p):
    """19 : 16 93
        | 89 27"""
    pass


def p_r43(p):
    """43 : 16 71
        | 89 36"""
    pass


def p_r117(p):
    """117 : 16 63
        | 89 40"""
    pass


def p_r110(p):
    """110 : 16 121
        | 89 92"""
    pass


def p_r122(p):
    """122 : 83 16
        | 84 89"""
    pass


def p_r37(p):
    """37 : 30 89
        | 21 16"""
    pass


def p_r128(p):
    """128 : 94 16
        | 44 89"""
    pass


def p_r46(p):
    """46 : 16 26
        | 89 94"""
    pass


def p_r7(p):
    """7 : 119 16
        | 28 89"""
    pass


def p_r31(p):
    """31 : 73 16
        | 14 89"""
    pass


def p_r0(p):
    """0 : 8 11"""
    pass


def p_r44(p):
    """44 : 89 16
        | 16 89"""
    pass


def p_r131(p):
    """131 : 18 16
        | 88 89"""
    pass


def p_r101(p):
    """101 : 16 100
        | 89 100"""
    pass


def p_r133(p):
    """133 : 89 109
        | 16 88"""
    pass


def p_r76(p):
    """76 : 89 72
        | 16 44"""
    pass


def p_r100(p):
    """100 : 89 89"""
    pass


def p_r93(p):
    """93 : 16 15
        | 89 123"""
    pass


def p_r138(p):
    """138 : 16 90
        | 89 122"""
    pass


def p_r89(p):
    """89 : A"""
    pass


def p_r47(p):
    """47 : 88 16
        | 72 89"""
    pass


def p_r96(p):
    """96 : 89 46
        | 16 131"""
    pass


def p_r48(p):
    """48 : 89 18
        | 16 72"""
    pass


def p_r39(p):
    """39 : 116 89
        | 139 16"""
    pass


def p_r103(p):
    """103 : 109 16
        | 100 89"""
    pass


def p_r121(p):
    """121 : 16 16
        | 89 87"""
    pass


def p_r86(p):
    """86 : 16 96
        | 89 125"""
    pass


def p_r123(p):
    """123 : 88 89
        | 100 16"""
    pass


def p_r84(p):
    """84 : 20 89
        | 104 16"""
    pass


def p_r49(p):
    """49 : 89 44
        | 16 26"""
    pass


def p_r4(p):
    """4 : 26 89
        | 109 16"""
    pass


def p_r33(p):
    """33 : 16 72
        | 89 26"""
    pass


def p_r75(p):
    """75 : 89 88
        | 16 94"""
    pass


def p_r28(p):
    """28 : 126 89
        | 76 16"""
    pass


def p_r9(p):
    """9 : 22 16
        | 129 89"""
    pass


def p_r98(p):
    """98 : 16 16"""
    pass


def p_r68(p):
    """68 : 16 101
        | 89 91"""
    pass


def p_r57(p):
    """57 : 88 16
        | 102 89"""
    pass


def p_r41(p):
    """41 : 106 16
        | 51 89"""
    pass


def p_r87(p):
    """87 : 16
        | 89"""
    pass


def p_r112(p):
    """112 : 74 89
        | 138 16"""
    pass


def p_r52(p):
    """52 : 72 16
        | 40 89"""
    pass


def p_r113(p):
    """113 : 89 24
        | 16 9"""
    pass


def p_r99(p):
    """99 : 109 89
        | 26 16"""
    pass


def p_r90(p):
    """90 : 2 89
        | 43 16"""
    pass


def p_r74(p):
    """74 : 105 16
        | 85 89"""
    pass


def p_r106(p):
    """106 : 89 18
        | 16 40"""
    pass


def p_r94(p):
    """94 : 89 16"""
    pass


def p_r13(p):
    """13 : 6 16
        | 34 89"""
    pass


def p_r91(p):
    """91 : 16 26"""
    pass


def p_r71(p):
    """71 : 44 89
        | 26 16"""
    pass


def p_r40(p):
    """40 : 87 16
        | 16 89"""
    pass


def p_r126(p):
    """126 : 89 94
        | 16 92"""
    pass


def p_r22(p):
    """22 : 89 75
        | 16 134"""
    pass


def p_error(p):
    if p:
        raise ValueError("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")
