# Creates a dictionary to convert number to a unique symbol and another dictionary to convert symbols into unique number
# Disclamer: Only characters that are 4 bytes or less can used in the mapping dictionary
#            Some of the newer emojis and new symbols may cause problems with the program 

import unicodedata as ud

# Creates a dictionary of unicode characters starting from 'start' and ending at 'end'
# createUnicodeDict will create a dictionary of (end - start) + 1 length as it includes the newline character

def is_valid(char):
    return ud.category(char) not in ('Cn', 'Cs', 'Co')

#print(is_valid('\u0378'))

def createUnicodeDict(start, end):
    dict_length = end - start
    
    dict_output = {}
    i = 0
    
    while (i < dict_length):
        
        if (is_valid(chr(start)) == True):
            dict_output[chr(start).encode("utf-8").decode("utf-8")] = i
            i+=1
            start+=1
        else:
            start+=1
    
    return dict_output
    

mapping_dict =   {
  "!": 0,
  "🂣": 1,
  "#": 2,
  "$": 3,
  "%": 4,
  "&": 5,
  "'": 6,
  "(": 7,
  ")": 8,
  "*": 9,
  "+": 10,
  ",": 11,
  "-": 12,
  ".": 13,
  "/": 14,
  "0": 15,
  "1": 16,
  "2": 17,
  "3": 18,
  "4": 19,
  "5": 20,
  "6": 21,
  "7": 22,
  "8": 23,
  "9": 24,
  ":": 25,
  ";": 26,
  "<": 27,
  "=": 28,
  ">": 29,
  "?": 30,
  "@": 31,
  "A": 32,
  "B": 33,
  "C": 34,
  "D": 35,
  "E": 36,
  "F": 37,
  "G": 38,
  "H": 39,
  "I": 40,
  "J": 41,
  "K": 42,
  "L": 43,
  "M": 44,
  "N": 45,
  "O": 46,
  "P": 47,
  "Q": 48,
  "R": 49,
  "S": 50,
  "T": 51,
  "U": 52,
  "V": 53,
  "W": 54,
  "X": 55,
  "Y": 56,
  "Z": 57,
  "[": 58,
  "\\": 59,
  "]": 60,
  "^": 61,
  "_": 62,
  "`": 63,
  "a": 64,
  "b": 65,
  "c": 66,
  "d": 67,
  "e": 68,
  "f": 69,
  "g": 70,
  "h": 71,
  "i": 72,
  "j": 73,
  "k": 74,
  "l": 75,
  "m": 76,
  "n": 77,
  "o": 78,
  "p": 79,
  "q": 80,
  "r": 81,
  "s": 82,
  "t": 83,
  "u": 84,
  "v": 85,
  "w": 86,
  "x": 87,
  "y": 88,
  "z": 89,
  "{": 90,
  "|": 91,
  "}": 92,
  "~": 93,
  "\u00a0": 94,
  "\u00a1": 95,
  "\u00a2": 96,
  "\u00a3": 97,
  "\u00a4": 98,
  "\u00a5": 99,
  "\u00a6": 100,
  "\u00a7": 101,
  "\u00a8": 102,
  "\u00a9": 103,
  "\u00aa": 104,
  "\u00ab": 105,
  "\u00ac": 106,
  "\u00ad": 107,
  "\u00ae": 108,
  "\u00af": 109,
  "\u00b0": 110,
  "\u00b1": 111,
  "\u00b2": 112,
  "\u00b3": 113,
  "\u00b4": 114,
  "\u00b5": 115,
  "\u00b6": 116,
  "\u00b7": 117,
  "\u00b8": 118,
  "\u00b9": 119,
  "\u00ba": 120,
  "\u00bb": 121,
  "\u00bc": 122,
  "\u00bd": 123,
  "\u00be": 124,
  "\u00bf": 125,
  "\u00c0": 126,
  "\u00c1": 127,
  "\u00c2": 128,
  "\u00c3": 129,
  "\u00c4": 130,
  "\u00c5": 131,
  "\u00c6": 132,
  "\u00c7": 133,
  "\u00c8": 134,
  "\u00c9": 135,
  "\u00ca": 136,
  "\u00cb": 137,
  "\u00cc": 138,
  "\u00cd": 139,
  "\u00ce": 140,
  "\u00cf": 141,
  "\u00d0": 142,
  "\u00d1": 143,
  "\u00d2": 144,
  "\u00d3": 145,
  "\u00d4": 146,
  "\u00d5": 147,
  "\u00d6": 148,
  "\u00d7": 149,
  "\u00d8": 150,
  "\u00d9": 151,
  "\u00da": 152,
  "\u00db": 153,
  "\u00dc": 154,
  "\u00dd": 155,
  "\u00de": 156,
  "\u00df": 157,
  "\u00e0": 158,
  "\u00e1": 159,
  "\u00e2": 160,
  "\u00e3": 161,
  "\u00e4": 162,
  "\u00e5": 163,
  "\u00e6": 164,
  "\u00e7": 165,
  "\u00e8": 166,
  "\u00e9": 167,
  "\u00ea": 168,
  "\u00eb": 169,
  "\u00ec": 170,
  "\u00ed": 171,
  "\u00ee": 172,
  "\u00ef": 173,
  "\u00f0": 174,
  "\u00f1": 175,
  "\u00f2": 176,
  "\u00f3": 177,
  "\u00f4": 178,
  "\u00f5": 179,
  "\u00f6": 180,
  "\u00f7": 181,
  "\u00f8": 182,
  "\u00f9": 183,
  "\u00fa": 184,
  "\u00fb": 185,
  "\u00fc": 186,
  "\u00fd": 187,
  "\u00fe": 188,
  "\u00ff": 189,
  "\u0100": 190,
  "\u0101": 191,
  "\u0102": 192,
  "\u0103": 193,
  "\u0104": 194,
  "\u0105": 195,
  "\u0106": 196,
  "\u0107": 197,
  "\u0108": 198,
  "\u0109": 199,
  "\u010a": 200,
  "\u010b": 201,
  "\u010c": 202,
  "\u010d": 203,
  "\u010e": 204,
  "\u010f": 205,
  "\u0110": 206,
  "\u0111": 207,
  "\u0112": 208,
  "\u0113": 209,
  "\u0114": 210,
  "\u0115": 211,
  "\u0116": 212,
  "\u0117": 213,
  "\u0118": 214,
  "\u0119": 215,
  "\u011a": 216,
  "\u011b": 217,
  "\u011c": 218,
  "\u011d": 219,
  "\u011e": 220,
  "\u011f": 221,
  "\u0120": 222,
  "\u0121": 223,
  "\u0122": 224,
  "\u0123": 225,
  "\u0124": 226,
  "\u0125": 227,
  "\u0126": 228,
  "\u0127": 229,
  "\u0128": 230,
  "\u0129": 231,
  "\u012a": 232,
  "\u012b": 233,
  "\u012c": 234,
  "\u012d": 235,
  "\u012e": 236,
  "\u012f": 237,
  "\u0130": 238,
  "\u0131": 239,
  "\u0132": 240,
  "\u0133": 241,
  "\u0134": 242,
  "\u0135": 243,
  "\u0136": 244,
  "\u0137": 245,
  "\u0138": 246,
  "\u0139": 247,
  "\u013a": 248,
  "\u013b": 249,
  "\u013c": 250,
  "\u013d": 251,
  "\u013e": 252,
  "\u013f": 253,
  "\u0140": 254,
  "\u0141": 255,
  "\u0142": 256,
  "\u0143": 257,
  "\u0144": 258,
  "\u0145": 259,
  "\u0146": 260,
  "\u0147": 261,
  "\u0148": 262,
  "\u0149": 263,
  "\u014a": 264,
  "\u014b": 265,
  "\u014c": 266,
  "\u014d": 267,
  "\u014e": 268,
  "\u014f": 269,
  "\u0150": 270,
  "\u0151": 271,
  "\u0152": 272,
  "\u0153": 273,
  "\u0154": 274,
  "\u0155": 275,
  "\u0156": 276,
  "\u0157": 277,
  "\u0158": 278,
  "\u0159": 279,
  "\u015a": 280,
  "\u015b": 281,
  "\u015c": 282,
  "\u015d": 283,
  "\u015e": 284,
  "\u015f": 285,
  "\u0160": 286,
  "\u0161": 287,
  "\u0162": 288,
  "\u0163": 289,
  "\u0164": 290,
  "\u0165": 291,
  "\u0166": 292,
  "\u0167": 293,
  "\u0168": 294,
  "\u0169": 295,
  "\u016a": 296,
  "\u016b": 297,
  "\u016c": 298,
  "\u016d": 299,
  "\u016e": 300,
  "\u016f": 301,
  "\u0170": 302,
  "\u0171": 303,
  "\u0172": 304,
  "\u0173": 305,
  "\u0174": 306,
  "\u0175": 307,
  "\u0176": 308,
  "\u0177": 309,
  "\u0178": 310,
  "\u0179": 311,
  "\u017a": 312,
  "\u017b": 313,
  "\u017c": 314,
  "\u017d": 315,
  "\u017e": 316,
  "\u017f": 317,
  "\u0180": 318,
  "\u0181": 319,
  "\u0182": 320,
  "\u0183": 321,
  "\u0184": 322,
  "\u0185": 323,
  "\u0186": 324,
  "\u0187": 325,
  "\u0188": 326,
  "\u0189": 327,
  "\u018a": 328,
  "\u018b": 329,
  "\u018c": 330,
  "\u018d": 331,
  "\u018e": 332,
  "\u018f": 333,
  "\u0190": 334,
  "\u0191": 335,
  "\u0192": 336,
  "\u0193": 337,
  "\u0194": 338,
  "\u0195": 339,
  "\u0196": 340,
  "\u0197": 341,
  "\u0198": 342,
  "\u0199": 343,
  "\u019a": 344,
  "\u019b": 345,
  "\u019c": 346,
  "\u019d": 347,
  "\u019e": 348,
  "\u019f": 349,
  "\u01a0": 350,
  "\u01a1": 351,
  "\u01a2": 352,
  "\u01a3": 353,
  "\u01a4": 354,
  "\u01a5": 355,
  "\u01a6": 356,
  "\u01a7": 357,
  "\u01a8": 358,
  "\u01a9": 359,
  "\u01aa": 360,
  "\u01ab": 361,
  "\u01ac": 362,
  "\u01ad": 363,
  "\u01ae": 364,
  "\u01af": 365,
  "\u01b0": 366,
  "\u01b1": 367,
  "\u01b2": 368,
  "\u01b3": 369,
  "\u01b4": 370,
  "\u01b5": 371,
  "\u01b6": 372,
  "\u01b7": 373,
  "\u01b8": 374,
  "\u01b9": 375,
  "\u01ba": 376,
  "\u01bb": 377,
  "\u01bc": 378,
  "\u01bd": 379,
  "\u01be": 380,
  "\u01bf": 381,
  "\u01c0": 382,
  "\u01c1": 383,
  "\u01c2": 384,
  "\u01c3": 385,
  "\u01c4": 386,
  "\u01c5": 387,
  "\u01c6": 388,
  "\u01c7": 389,
  "\u01c8": 390,
  "\u01c9": 391,
  "\u01ca": 392,
  "\u01cb": 393,
  "\u01cc": 394,
  "\u01cd": 395,
  "\u01ce": 396,
  "\u01cf": 397,
  "\u01d0": 398,
  "\u01d1": 399,
  "\u01d2": 400,
  "\u01d3": 401,
  "\u01d4": 402,
  "\u01d5": 403,
  "\u01d6": 404,
  "\u01d7": 405,
  "\u01d8": 406,
  "\u01d9": 407,
  "\u01da": 408,
  "\u01db": 409,
  "\u01dc": 410,
  "\u01dd": 411,
  "\u01de": 412,
  "\u01df": 413,
  "\u01e0": 414,
  "\u01e1": 415,
  "\u01e2": 416,
  "\u01e3": 417,
  "\u01e4": 418,
  "\u01e5": 419,
  "\u01e6": 420,
  "\u01e7": 421,
  "\u01e8": 422,
  "\u01e9": 423,
  "\u01ea": 424,
  "\u01eb": 425,
  "\u01ec": 426,
  "\u01ed": 427,
  "\u01ee": 428,
  "\u01ef": 429,
  "\u01f0": 430,
  "\u01f1": 431,
  "\u01f2": 432,
  "\u01f3": 433,
  "\u01f4": 434,
  "\u01f5": 435,
  "\u01f6": 436,
  "\u01f7": 437,
  "\u01f8": 438,
  "\u01f9": 439,
  "\u01fa": 440,
  "\u01fb": 441,
  "\u01fc": 442,
  "\u01fd": 443,
  "\u01fe": 444,
  "\u01ff": 445,
  "\u0200": 446,
  "\u0201": 447,
  "\u0202": 448,
  "\u0203": 449,
  "\u0204": 450,
  "\u0205": 451,
  "\u0206": 452,
  "\u0207": 453,
  "\u0208": 454,
  "\u0209": 455,
  "\u020a": 456,
  "\u020b": 457,
  "\u020c": 458,
  "\u020d": 459,
  "\u020e": 460,
  "\u020f": 461,
  "\u0210": 462,
  "\u0211": 463,
  "\u0212": 464,
  "\u0213": 465,
  "\u0214": 466,
  "\u0215": 467,
  "\u0216": 468,
  "\u0217": 469,
  "\u0218": 470,
  "\u0219": 471,
  "\u021a": 472,
  "\u021b": 473,
  "\u021c": 474,
  "\u021d": 475,
  "\u021e": 476,
  "\u021f": 477,
  "\u0220": 478,
  "\u0221": 479,
  "\u0222": 480,
  "\u0223": 481,
  "\u0224": 482,
  "\u0225": 483,
  "\u0226": 484,
  "\u0227": 485,
  "\u0228": 486,
  "\u0229": 487,
  "\u022a": 488,
  "\u022b": 489,
  "\u022c": 490,
  "\u022d": 491,
  "\u022e": 492,
  "\u022f": 493,
  "\u0230": 494,
  "\u0231": 495,
  "\u0232": 496,
  "\u0233": 497,
  "\u0234": 498,
  "\u0235": 499,
  "\u0236": 500,
  "\u0237": 501,
  "\u0238": 502,
  "\u0239": 503,
  "\u023a": 504,
  "\u023b": 505,
  "\u023c": 506,
  "\u023d": 507,
  "\u023e": 508,
  "\u023f": 509,
  "\u0240": 510,
  "\u0241": 511,
  "\u0242": 512,
  "\u0243": 513,
  "\u0244": 514,
  "\u0245": 515,
  "\u0246": 516,
  "\u0247": 517,
  "\u0248": 518,
  "\u0249": 519,
  "\u024a": 520,
  "\u024b": 521,
  "\u024c": 522,
  "\u024d": 523,
  "\u024e": 524,
  "\u024f": 525,
  "\u0250": 526,
  "\u0251": 527,
  "\u0252": 528,
  "\u0253": 529,
  "\u0254": 530,
  "\u0255": 531,
  "\u0256": 532,
  "\u0257": 533,
  "\u0258": 534,
  "\u0259": 535,
  "\u025a": 536,
  "\u025b": 537,
  "\u025c": 538,
  "\u025d": 539,
  "\u025e": 540,
  "\u025f": 541,
  "\u0260": 542,
  "\u0261": 543,
  "\u0262": 544,
  "\u0263": 545,
  "\u0264": 546,
  "\u0265": 547,
  "\u0266": 548,
  "\u0267": 549,
  "\u0268": 550,
  "\u0269": 551,
  "\u026a": 552,
  "\u026b": 553,
  "\u026c": 554,
  "\u026d": 555,
  "\u026e": 556,
  "\u026f": 557,
  "\u0270": 558,
  "\u0271": 559,
  "\u0272": 560,
  "\u0273": 561,
  "\u0274": 562,
  "\u0275": 563,
  "\u0276": 564,
  "\u0277": 565,
  "\u0278": 566,
  "\u0279": 567,
  "\u027a": 568,
  "\u027b": 569,
  "\u027c": 570,
  "\u027d": 571,
  "\u027e": 572,
  "\u027f": 573,
  "\u0280": 574,
  "\u0281": 575,
  "\u0282": 576,
  "\u0283": 577,
  "\u0284": 578,
  "\u0285": 579,
  "\u0286": 580,
  "\u0287": 581,
  "\u0288": 582,
  "\u0289": 583,
  "\u028a": 584,
  "\u028b": 585,
  "\u028c": 586,
  "\u028d": 587,
  "\u028e": 588,
  "\u028f": 589,
  "\u0290": 590,
  "\u0291": 591,
  "\u0292": 592,
  "\u0293": 593,
  "\u0294": 594,
  "\u0295": 595,
  "\u0296": 596,
  "\u0297": 597,
  "\u0298": 598,
  "\u0299": 599,
  "\u029a": 600,
  "\u029b": 601,
  "\u029c": 602,
  "\u029d": 603,
  "\u029e": 604,
  "\u029f": 605,
  "\u02a0": 606,
  "\u02a1": 607,
  "\u02a2": 608,
  "\u02a3": 609,
  "\u02a4": 610,
  "\u02a5": 611,
  "\u02a6": 612,
  "\u02a7": 613,
  "\u02a8": 614,
  "\u02a9": 615,
  "\u02aa": 616,
  "\u02ab": 617,
  "\u02ac": 618,
  "\u02ad": 619,
  "\u02ae": 620,
  "\u02af": 621,
  "\u02b0": 622,
  "\u02b1": 623,
  "\u02b2": 624,
  "\u02b3": 625,
  "\u02b4": 626,
  "\u02b5": 627,
  "\u02b6": 628,
  "\u02b7": 629,
  "\u02b8": 630,
  "\u02b9": 631,
  "\u02ba": 632,
  "\u02bb": 633,
  "\u02bc": 634,
  "\u02bd": 635,
  "\u02be": 636,
  "\u02bf": 637,
  "\u02c0": 638,
  "\u02c1": 639,
  "\u02c2": 640,
  "\u02c3": 641,
  "\u02c4": 642,
  "\u02c5": 643,
  "\u02c6": 644,
  "\u02c7": 645,
  "\u02c8": 646,
  "\u02c9": 647,
  "\u02ca": 648,
  "\u02cb": 649,
  "\u02cc": 650,
  "\u02cd": 651,
  "\u02ce": 652,
  "\u02cf": 653,
  "\u02d0": 654,
  "\u02d1": 655,
  "\u02d2": 656,
  "\u02d3": 657,
  "\u02d4": 658,
  "\u02d5": 659,
  "\u02d6": 660,
  "\u02d7": 661,
  "\u02d8": 662,
  "\u02d9": 663,
  "\u02da": 664,
  "\u02db": 665,
  "\u02dc": 666,
  "\u02dd": 667,
  "\u02de": 668,
  "\u02df": 669,
  "\u02e0": 670,
  "\u02e1": 671,
  "\u02e2": 672,
  "\u02e3": 673,
  "\u02e4": 674,
  "\u02e5": 675,
  "\u02e6": 676,
  "\u02e7": 677,
  "\u02e8": 678,
  "\u02e9": 679,
  "\u02ea": 680,
  "\u02eb": 681,
  "\u02ec": 682,
  "\u02ed": 683,
  "\u02ee": 684,
  "\u02ef": 685,
  "\u02f0": 686,
  "\u02f1": 687,
  "\u02f2": 688,
  "\u02f3": 689,
  "\u02f4": 690,
  "\u02f5": 691,
  "\u02f6": 692,
  "\u02f7": 693,
  "\u02f8": 694,
  "\u02f9": 695,
  "\u02fa": 696,
  "\u02fb": 697,
  "\u02fc": 698,
  "\u02fd": 699,
  "\u02fe": 700,
  "\u02ff": 701,
  "\u0300": 702,
  "\u0301": 703,
  "\u0302": 704,
  "\u0303": 705,
  "\u0304": 706,
  "\u0305": 707,
  "\u0306": 708,
  "\u0307": 709,
  "\u0308": 710,
  "\u0309": 711,
  "\u030a": 712,
  "\u030b": 713,
  "\u030c": 714,
  "\u030d": 715,
  "\u030e": 716,
  "\u030f": 717,
  "\u0310": 718,
  "\u0311": 719,
  "\u0312": 720,
  "\u0313": 721,
  "\u0314": 722,
  "\u0315": 723,
  "\u0316": 724,
  "\u0317": 725,
  "\u0318": 726,
  "\u0319": 727,
  "\u031a": 728,
  "\u031b": 729,
  "\u031c": 730,
  "\u031d": 731,
  "\u031e": 732,
  "\u031f": 733,
  "\u0320": 734,
  "\u0321": 735,
  "\u0322": 736,
  "\u0323": 737,
  "\u0324": 738,
  "\u0325": 739,
  "\u0326": 740,
  "\u0327": 741,
  "\u0328": 742,
  "\u0329": 743,
  "\u032a": 744,
  "\u032b": 745,
  "\u032c": 746,
  "\u032d": 747,
  "\u032e": 748,
  "\u032f": 749,
  "\u0330": 750,
  "\u0331": 751,
  "\u0332": 752,
  "\u0333": 753,
  "\u0334": 754,
  "\u0335": 755,
  "\u0336": 756,
  "\u0337": 757,
  "\u0338": 758,
  "\u0339": 759,
  "\u033a": 760,
  "\u033b": 761,
  "\u033c": 762,
  "\u033d": 763,
  "\u033e": 764,
  "\u033f": 765,
  "\u0340": 766,
  "\u0341": 767,
  "\u0342": 768,
  "\u0343": 769,
  "\u0344": 770,
  "\u0345": 771,
  "\u0346": 772,
  "\u0347": 773,
  "\u0348": 774,
  "\u0349": 775,
  "\u034a": 776,
  "\u034b": 777,
  "\u034c": 778,
  "\u034d": 779,
  "\u034e": 780,
  "\u034f": 781,
  "\u0350": 782,
  "\u0351": 783,
  "\u0352": 784,
  "\u0353": 785,
  "\u0354": 786,
  "\u0355": 787,
  "\u0356": 788,
  "\u0357": 789,
  "\u0358": 790,
  "\u0359": 791,
  "\u035a": 792,
  "\u035b": 793,
  "\u035c": 794,
  "\u035d": 795,
  "\u035e": 796,
  "\u035f": 797,
  "\u0360": 798,
  "\u0361": 799,
  "\u0362": 800,
  "\u0363": 801,
  "\u0364": 802,
  "\u0365": 803,
  "\u0366": 804,
  "\u0367": 805,
  "\u0368": 806,
  "\u0369": 807,
  "\u036a": 808,
  "\u036b": 809,
  "\u036c": 810,
  "\u036d": 811,
  "\u036e": 812,
  "\u036f": 813,
  "\u0370": 814,
  "\u0371": 815,
  "\u0372": 816,
  "\u0373": 817,
  "\u0374": 818,
  "\u0375": 819,
  "\u0376": 820,
  "\u0377": 821,
  "\u0378": 822,
  "\u0379": 823,
  "\u037a": 824,
  "\u037b": 825,
  "\u037c": 826,
  "\u037d": 827,
  "\u037e": 828,
  "\u037f": 829,
  "\u0380": 830,
  "\u0381": 831,
  "\u0382": 832,
  "\u0383": 833,
  "\u0384": 834,
  "\u0385": 835,
  "\u0386": 836,
  "\u0387": 837,
  "\u0388": 838,
  "\u0389": 839,
  "\u038a": 840,
  "\u038b": 841,
  "\u038c": 842,
  "\u038d": 843,
  "\u038e": 844,
  "\u038f": 845,
  "\u0390": 846,
  "\u0391": 847,
  "\u0392": 848,
  "\u0393": 849,
  "\u0394": 850,
  "\u0395": 851,
  "\u0396": 852,
  "\u0397": 853,
  "\u0398": 854,
  "\u0399": 855,
  "\u039a": 856,
  "\u039b": 857,
  "\u039c": 858,
  "\u039d": 859,
  "\u039e": 860,
  "\u039f": 861,
  "\u03a0": 862,
  "\u03a1": 863,
  "\u03a2": 864,
  "\u03a3": 865,
  "\u03a4": 866,
  "\u03a5": 867,
  "\u03a6": 868,
  "\u03a7": 869,
  "\u03a8": 870,
  "\u03a9": 871,
  "\u03aa": 872,
  "\u03ab": 873,
  "\u03ac": 874,
  "\u03ad": 875,
  "\u03ae": 876,
  "\u03af": 877,
  "\u03b0": 878,
  "\u03b1": 879,
  "\u03b2": 880,
  "\u03b3": 881,
  "\u03b4": 882,
  "\u03b5": 883,
  "\u03b6": 884,
  "\u03b7": 885,
  "\u03b8": 886,
  "\u03b9": 887,
  "\u03ba": 888,
  "\u03bb": 889,
  "\u03bc": 890,
  "\u03bd": 891,
  "\u03be": 892,
  "\u03bf": 893,
  "\u03c0": 894,
  "\u03c1": 895,
  "\u03c2": 896,
  "\u03c3": 897,
  "\u03c4": 898,
  "\u03c5": 899,
  "\u03c6": 900,
  "\u03c7": 901,
  "\u03c8": 902,
  "\u03c9": 903,
  "\u03ca": 904,
  "\u03cb": 905,
  "\u03cc": 906,
  "\u03cd": 907,
  "\u03ce": 908,
  "\u03cf": 909,
  "\u03d0": 910,
  "\u03d1": 911,
  "\u03d2": 912,
  "\u03d3": 913,
  "\u03d4": 914,
  "\u03d5": 915,
  "\u03d6": 916,
  "\u03d7": 917,
  "\u03d8": 918,
  "\u03d9": 919,
  "\u03da": 920,
  "\u03db": 921,
  "\u03dc": 922,
  "\u03dd": 923,
  "\u03de": 924,
  "\u03df": 925,
  "\u03e0": 926,
  "\u03e1": 927,
  "\u03e2": 928,
  "\u03e3": 929,
  "\u03e4": 930,
  "\u03e5": 931,
  "\u03e6": 932,
  "\u03e7": 933,
  "\u03e8": 934,
  "\u03e9": 935,
  "\u03ea": 936,
  "\u03eb": 937,
  "\u03ec": 938,
  "\u03ed": 939,
  "\u03ee": 940,
  "\u03ef": 941,
  "\u03f0": 942,
  "\u03f1": 943,
  "\u03f2": 944,
  "\u03f3": 945,
  "\u03f4": 946,
  "\u03f5": 947,
  "\u03f6": 948,
  "\u03f7": 949,
  "\u03f8": 950,
  "\u03f9": 951,
  "\u03fa": 952,
  "\u03fb": 953,
  "\u03fc": 954,
  "\u03fd": 955,
  "\u03fe": 956,
  "\u03ff": 957,
  "\u0400": 958,
  "\u0401": 959,
  "\u0402": 960,
  "\u0403": 961,
  "\u0404": 962,
  "\u0405": 963,
  "\u0406": 964,
  "\u0407": 965,
  "\u0408": 966,
  "\u0409": 967,
  "\u040a": 968,
  "\u040b": 969,
  "\u040c": 970,
  "\u040d": 971,
  "\u040e": 972,
  "\u040f": 973,
  "\u0410": 974,
  "\u0411": 975,
  "\u0412": 976,
  "\u0413": 977,
  "\u0414": 978,
  "\u0415": 979,
  "\u0416": 980,
  "\u0417": 981,
  "\u0418": 982,
  "\u0419": 983,
  "\u041a": 984,
  "\u041b": 985,
  "\u041c": 986,
  "\u041d": 987,
  "\u041e": 988,
  "\u041f": 989,
  "\u0420": 990,
  "\u0421": 991,
  "\u0422": 992,
  "\u0423": 993,
  "\u0424": 994,
  "\u0425": 995,
  "\u0426": 996,
  "\u0427": 997,
  "\u0428": 998,
  "\u0429": 999,
}

# Creating mapping dictionary
mapping_dict = createUnicodeDict(32,1032)

# Inversed Dictionary for reverse serach
inv_mapping_dict = {v: k for k, v in mapping_dict.items()}
#print(mapping_dict)
