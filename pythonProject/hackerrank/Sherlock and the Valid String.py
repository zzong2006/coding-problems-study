#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the isValid function below.
def isValid(s):
    cnt = Counter(s)
    print(cnt)
    cnt = Counter(cnt.values())
    print(cnt)
    keys = cnt.keys()
    if len(keys) > 2:
        return "NO"
    elif len(keys) == 1:
        return "YES"
    elif len(keys) == 2:
        a, b = keys
        if (
            (a == 1 and cnt[a] == 1)
            or (b == 1 and cnt[b] == 1)
            or (b - a == 1 and cnt[b] == 1)
            or (a - b == 1 and cnt[a] == 1)
        ):
            return "YES"
        else:
            return "NO"
    return "YES"


if __name__ == "__main__":
    s = (
        "ebhcgicceggecgdcibbeicigehhebabiehbdgaeaigihghbhigihfebgabicbgfhhedgbfehiahchcecedffhccebifcbdf"
        "cfaecicafahfiecceeaabbecfhgbfifabbffadcieeaiidddhfdeccaedbgcfdehbadihheieidgcfbdiiicgahebfbbdfe"
        "ffegbdhgdagefhbgafaabfghdcbfdhabhfahbdhgifbghhafcieachcbeabccbiigdcfegcccfafehegbiecbdhabcffgg"
        "iifaabfagbfdfbfacdcafabccgibiidgabiabigbgbbaideeagaaffcddhieicehhchfedfgbgbfhgedhacegaieeedgga"
        "cbbgadeibbbcdhbabbieibcfbhgdbbiecdhbffaghhchhddcihgdgbgdcfgfggeaahffgiddeadgcegaiddhhdgagdidga"
        "cafececiebeigcbdfaedibbgbhciihcdifbacdagfbcefifefchhddadeaiegbfaidbeebiefghfghhdabdeegabagfbbdg"
        "beaiiigeaadhbgebedddfihagdeiccdbcfchgadhgfaidaebfabbagdghebgagbfhfbgeagdgecbhfchebdgafceaffabag"
        "edbhcgcedaecdbiifefchcbgfbbibhiahchhfadffeacfbgeigaccedadaafhcieficdfhfheibfdhbgbfhhdfcghabacgg"
        "chchbdaigbcihhdbifcdeggicgacehebadbdaibhdciefdgfhfeggdhgcaeeeidfebbaicgagcaiachffhadbddhhdbcehci"
        "agfdgeadidfcaaiafeadefbbbaidgiagbeacchbdaifgccgcfigefcachiiggbghfhbifciafgfigaabidhdgffcbgicbidi"
        "bacbgfhddafbegdaagbhddceeifecciddigfiehdbdabahgaechffidebhicfcciahhchebdbei"
    )
    s = "aaab"

    result = isValid(s)
    print(result)
