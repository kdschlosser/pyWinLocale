# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2018 EventGhost Project <http://eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

import ctypes
import os
import sys
import locale as _locale
from ctypes.wintypes import LCID, DWORD, INT, WCHAR

try:
    wx = __import__('wx')

    LCID_TO_WX = {

        # Default custom sublanguage
        # sub: SUBLANG_CUSTOM_DEFAULT primary: LANG_NEUTRAL
        0x0C00: wx.LANGUAGE_DEFAULT,

        # no x-ref wx.LANGUAGE_ABKHAZIAN
        # no x-ref wx.LANGUAGE_AFAR

        # South Africa (ZA)
        # sub: SUBLANG_AFRIKAANS_SOUTH_AFRICA primary: LANG_AFRIKAANS
        0x0436: wx.LANGUAGE_AFRIKAANS,

        # Albania (AL)
        # sub: SUBLANG_ALBANIAN_ALBANIA primary: LANG_ALBANIAN
        0x041C: wx.LANGUAGE_ALBANIAN,

        # Ethiopia (ET)
        # sub: SUBLANG_AMHARIC_ETHIOPIA primary: LANG_AMHARIC
        0x045E: wx.LANGUAGE_AMHARIC,

        # Algeria (DZ)
        # sub: SUBLANG_ARABIC_ALGERIA primary: LANG_ARABIC
        0x1401: wx.LANGUAGE_ARABIC_ALGERIA,

        # Bahrain (BH)
        # sub: SUBLANG_ARABIC_BAHRAIN primary: LANG_ARABIC
        0x3C01: wx.LANGUAGE_ARABIC_BAHRAIN,

        # Egypt (EG)
        # sub: SUBLANG_ARABIC_EGYPT primary: LANG_ARABIC
        0x0C01: wx.LANGUAGE_ARABIC_EGYPT,

        # Iraq (IQ)
        # sub: SUBLANG_ARABIC_IRAQ primary: LANG_ARABIC
        0x0801: wx.LANGUAGE_ARABIC_IRAQ,

        # Jordan (JO)
        # sub: SUBLANG_ARABIC_JORDAN primary: LANG_ARABIC
        0x2C01: wx.LANGUAGE_ARABIC_JORDAN,

        # Kuwait (KW)
        # sub: SUBLANG_ARABIC_KUWAIT primary: LANG_ARABIC
        0x3401: wx.LANGUAGE_ARABIC_KUWAIT,

        # Lebanon (LB)
        # sub: SUBLANG_ARABIC_LEBANON primary: LANG_ARABIC
        0x3001: wx.LANGUAGE_ARABIC_LEBANON,

        # Libya (LY)
        # sub: SUBLANG_ARABIC_LIBYA primary: LANG_ARABIC
        0x1001: wx.LANGUAGE_ARABIC_LIBYA,

        # Morocco (MA)
        # sub: SUBLANG_ARABIC_MOROCCO primary: LANG_ARABIC
        0x1801: wx.LANGUAGE_ARABIC_MOROCCO,

        # Oman (OM)
        # sub: SUBLANG_ARABIC_OMAN primary: LANG_ARABIC
        0x2001: wx.LANGUAGE_ARABIC_OMAN,

        # Qatar (QA)
        # sub: SUBLANG_ARABIC_QATAR primary: LANG_ARABIC
        0x4001: wx.LANGUAGE_ARABIC_QATAR,

        # Saudi Arabia (SA)
        # sub: SUBLANG_ARABIC_SAUDI_ARABIA primary: LANG_ARABIC
        0x0401: wx.LANGUAGE_ARABIC_SAUDI_ARABIA,

        # no x-ref wx.LANGUAGE_ARABIC_SUDAN

        # Syria (SY)
        # sub: SUBLANG_ARABIC_SYRIA primary: LANG_ARABIC
        0x2801: wx.LANGUAGE_ARABIC_SYRIA,

        # Tunisia (TN)
        # sub: SUBLANG_ARABIC_TUNISIA primary: LANG_ARABIC
        0x1C01: wx.LANGUAGE_ARABIC_TUNISIA,

        # U.A.E. (AE)
        # sub: SUBLANG_ARABIC_UAE primary: LANG_ARABIC
        0x3801: wx.LANGUAGE_ARABIC_UAE,

        # Yemen (YE)
        # sub: SUBLANG_ARABIC_YEMEN primary: LANG_ARABIC
        0x2401: wx.LANGUAGE_ARABIC_YEMEN,

        # Armenia (AM)
        # sub: SUBLANG_ARMENIAN_ARMENIA primary: LANG_ARMENIAN
        0x042B: wx.LANGUAGE_ARMENIAN,

        # India (IN)
        # sub: SUBLANG_ASSAMESE_INDIA primary: LANG_ASSAMESE
        0x044D: wx.LANGUAGE_ASSAMESE,

        # no x-ref wx.LANGUAGE_ASTURIAN
        # no x-ref wx.LANGUAGE_AYMARA

        # Azerbaijan, Cyrillic (AZ)
        # sub: SUBLANG_AZERI_CYRILLIC primary: LANG_AZERI
        0x082C: wx.LANGUAGE_AZERI_CYRILLIC,

        # Azerbaijan, Latin (AZ)
        # sub: SUBLANG_AZERI_LATIN primary: LANG_AZERI
        0x042C: wx.LANGUAGE_AZERI_LATIN,

        # Russia (RU)
        # sub: SUBLANG_BASHKIR_RUSSIA primary: LANG_BASHKIR
        0x046D: wx.LANGUAGE_BASHKIR,

        # Basque (Basque)
        # sub: SUBLANG_BASQUE_BASQUE primary: LANG_BASQUE
        0x042D: wx.LANGUAGE_BASQUE,

        # Belarus (BY)
        # sub: SUBLANG_BELARUSIAN_BELARUS primary: LANG_BELARUSIAN
        0x0423: wx.LANGUAGE_BELARUSIAN,

        # no x-ref wx.LANGUAGE_BENGALI
        # no x-ref wx.LANGUAGE_BHUTANI
        # no x-ref wx.LANGUAGE_BIHARI
        # no x-ref wx.LANGUAGE_BISLAMA

        # Bosnia and Herzegovina, Cyrillic (BA)
        # sub:  primary: LANG_BOSNIAN_NEUTRAL
        # 0x781A: wx.LANGUAGE_BOSNIAN,

        # France (FR)
        # sub: SUBLANG_BRETON_FRANCE primary: LANG_BRETON
        0x047E: wx.LANGUAGE_BRETON,

        # Bulgaria (BG)
        # sub: SUBLANG_BULGARIAN_BULGARIA primary: LANG_BULGARIAN
        0x0402: wx.LANGUAGE_BULGARIAN,

        # no x-ref wx.LANGUAGE_BURMESE

        # Iraq (IQ)
        # sub: SUBLANG_CENTRAL_KURDISH_IRAQ primary: LANG_CENTRAL_KURDISH
        0x0492: wx.LANGUAGE_KURDISH,

        # no x-ref wx.LANGUAGE_CAMBODIAN

        # Spain (ES)
        # sub: SUBLANG_CATALAN_CATALAN primary: LANG_CATALAN
        0x0403: wx.LANGUAGE_CATALAN,

        # Hong Kong SAR, PRC (HK)
        # sub: SUBLANG_CHINESE_HONGKONG primary: LANG_CHINESE
        0x0C04: wx.LANGUAGE_CHINESE_HONGKONG,

        # Macao SAR (MO)
        # sub: SUBLANG_CHINESE_MACAU primary: LANG_CHINESE
        0x1404: wx.LANGUAGE_CHINESE_MACAU,

        # Singapore (SG)
        # sub: SUBLANG_CHINESE_SINGAPORE primary: LANG_CHINESE
        0x1004: wx.LANGUAGE_CHINESE_SINGAPORE,

        # Simplified (Hans)
        # sub: SUBLANG_CHINESE_SIMPLIFIED primary: LANG_CHINESE_SIMPLIFIED
        0x0004: wx.LANGUAGE_CHINESE_SIMPLIFIED,

        # no x-ref wx.LANGUAGE_CHINESE_TAIWAN

        # Traditional (Hant)
        # sub: SUBLANG_CHINESE_TRADITIONAL primary: LANG_CHINESE_TRADITIONAL
        0x7C04: wx.LANGUAGE_CHINESE_TRADITIONAL,

        # France (FR)
        # sub: SUBLANG_CORSICAN_FRANCE primary: LANG_CORSICAN
        0x0483: wx.LANGUAGE_CORSICAN,

        # Croatia (HR)
        # sub: SUBLANG_CROATIAN_CROATIA primary: LANG_CROATIAN
        0x041A: wx.LANGUAGE_CROATIAN,

        # Czech Republic (CZ)
        # sub: SUBLANG_CZECH_CZECH_REPUBLIC primary: LANG_CZECH
        0x0405: wx.LANGUAGE_CZECH,

        # Denmark (DK)
        # sub: SUBLANG_DANISH_DENMARK primary: LANG_DANISH
        0x0406: wx.LANGUAGE_DANISH,

        # Netherlands (NL)
        # sub: SUBLANG_DUTCH primary: LANG_DUTCH
        0x0413: wx.LANGUAGE_DUTCH,

        # Belgium (BE)
        # sub: SUBLANG_DUTCH_BELGIAN primary: LANG_DUTCH
        0x0813: wx.LANGUAGE_DUTCH_BELGIAN,

        # Australia (AU)
        # sub: SUBLANG_ENGLISH_AUS primary: LANG_ENGLISH
        0x0C09: wx.LANGUAGE_ENGLISH_AUSTRALIA,

        # Belize (BZ)
        # sub: SUBLANG_ENGLISH_BELIZE primary: LANG_ENGLISH
        0x2809: wx.LANGUAGE_ENGLISH_BELIZE,

        # no x-ref wx.LANGUAGE_ENGLISH_BOTSWANA

        # Canada (CA)
        # sub: SUBLANG_ENGLISH_CAN primary: LANG_ENGLISH
        0x1009: wx.LANGUAGE_ENGLISH_CANADA,

        # Caribbean (029)
        # sub: SUBLANG_ENGLISH_CARIBBEAN primary: LANG_ENGLISH
        0x2409: wx.LANGUAGE_ENGLISH_CARIBBEAN,

        # no x-ref wx.LANGUAGE_ENGLISH_DENMARK

        # Ireland (IE); see note 3
        # sub: SUBLANG_ENGLISH_EIRE primary: LANG_ENGLISH
        0x1809: wx.LANGUAGE_ENGLISH_EIRE,

        # Jamaica (JM)
        # sub: SUBLANG_ENGLISH_JAMAICA primary: LANG_ENGLISH
        0x2009: wx.LANGUAGE_ENGLISH_JAMAICA,

        # Malaysia (MY)
        # sub: SUBLANG_ENGLISH_MALAYSIA primary: LANG_ENGLISH
        0x4409: wx.LANGUAGE_MALAY,

        # New Zealand (NZ)
        # sub: SUBLANG_ENGLISH_NZ primary: LANG_ENGLISH
        0x1409: wx.LANGUAGE_ENGLISH_NEW_ZEALAND,

        # Philippines (PH)
        # sub: SUBLANG_ENGLISH_PHILIPPINES primary: LANG_ENGLISH
        0x3409: wx.LANGUAGE_ENGLISH_PHILIPPINES,

        # South Africa (ZA)
        # sub: SUBLANG_ENGLISH_SOUTH_AFRICA primary: LANG_ENGLISH
        0x1c09: wx.LANGUAGE_ENGLISH_SOUTH_AFRICA,

        # Trinidad and Tobago (TT)
        # sub: SUBLANG_ENGLISH_TRINIDAD primary: LANG_ENGLISH
        0x2C09: wx.LANGUAGE_ENGLISH_TRINIDAD,

        # United Kingdom (GB)
        # sub: SUBLANG_ENGLISH_UK primary: LANG_ENGLISH
        0x0809: wx.LANGUAGE_ENGLISH_UK,

        # United States (US)
        # sub: SUBLANG_ENGLISH_US primary: LANG_ENGLISH
        0x0409: wx.LANGUAGE_ENGLISH_US,

        # Zimbabwe (ZW)
        # sub: SUBLANG_ENGLISH_ZIMBABWE primary: LANG_ENGLISH
        0x3009: wx.LANGUAGE_ENGLISH_ZIMBABWE,

        # no x-ref wx.LANGUAGE_ESPERANTO

        # Estonia (EE)
        # sub: SUBLANG_ESTONIAN_ESTONIA primary: LANG_ESTONIAN
        0x0425: wx.LANGUAGE_ESTONIAN,

        # Faroe Islands (FO)
        # sub: SUBLANG_FAEROESE_FAROE_ISLANDS primary: LANG_FAEROESE
        0x0438: wx.LANGUAGE_FAEROESE,

        # no x-ref wx.LANGUAGE_FARSI
        # no x-ref wx.LANGUAGE_FIJI

        # Finland (FI)
        # sub: SUBLANG_FINNISH_FINLAND primary: LANG_FINNISH
        0x040B: wx.LANGUAGE_FINNISH,

        # Belgium (BE)
        # sub: SUBLANG_FRENCH_BELGIAN primary: LANG_FRENCH
        0x080c: wx.LANGUAGE_FRENCH_BELGIAN,

        # Canada (CA)
        # sub: SUBLANG_FRENCH_CANADIAN primary: LANG_FRENCH
        0x0C0C: wx.LANGUAGE_FRENCH_CANADIAN,

        # France (FR)
        # sub: SUBLANG_FRENCH primary: LANG_FRENCH
        0x040c: wx.LANGUAGE_FRENCH,

        # Luxembourg (LU)
        # sub: SUBLANG_FRENCH_LUXEMBOURG primary: LANG_FRENCH
        0x140C: wx.LANGUAGE_FRENCH_LUXEMBOURG,

        # Monaco (MC)
        # sub: SUBLANG_FRENCH_MONACO primary: LANG_FRENCH
        0x180C: wx.LANGUAGE_FRENCH_MONACO,

        # Switzerland (CH)
        # sub: SUBLANG_FRENCH_SWISS primary: LANG_FRENCH
        0x100C: wx.LANGUAGE_FRENCH_SWISS,

        # Netherlands (NL)
        # sub: SUBLANG_FRISIAN_NETHERLANDS primary: LANG_FRISIAN
        0x0462: wx.LANGUAGE_FRISIAN,

        # Spain (ES)
        # sub: SUBLANG_GALICIAN_GALICIAN primary: LANG_GALICIAN
        0x0456: wx.LANGUAGE_GALICIAN,

        # Georgia (GE)
        # sub: SUBLANG_GEORGIAN_GEORGIA primary: LANG_GEORGIAN
        0x0437: wx.LANGUAGE_GEORGIAN,

        # Austria (AT)
        # sub: SUBLANG_GERMAN_AUSTRIAN primary: LANG_GERMAN
        0x0C07: wx.LANGUAGE_GERMAN_AUSTRIAN,

        # Germany (DE)
        # sub: SUBLANG_GERMAN primary: LANG_GERMAN
        0x0407: wx.LANGUAGE_GERMAN,

        # no x-ref wx.LANGUAGE_GERMAN_BELGIUM

        # Liechtenstein (LI)
        # sub: SUBLANG_GERMAN_LIECHTENSTEIN primary: LANG_GERMAN
        0x1407: wx.LANGUAGE_GERMAN_LIECHTENSTEIN,

        # Luxembourg (LU)
        # sub: SUBLANG_GERMAN_LUXEMBOURG primary: LANG_GERMAN
        0x1007: wx.LANGUAGE_GERMAN_LUXEMBOURG,

        # Switzerland (CH)
        # sub: SUBLANG_GERMAN_SWISS primary: LANG_GERMAN
        0x0807: wx.LANGUAGE_GERMAN_SWISS,

        # Greece (GR)
        # sub: SUBLANG_GREEK_GREECE primary: LANG_GREEK
        0x0408: wx.LANGUAGE_GREEK,

        # Greenland (GL)
        # sub: SUBLANG_GREENLANDIC_GREENLAND primary: LANG_GREENLANDIC
        0x046F: wx.LANGUAGE_GREENLANDIC,

        # no x-ref wx.LANGUAGE_GUARANI

        # India (IN)
        # sub: SUBLANG_GUJARATI_INDIA primary: LANG_GUJARATI
        0x0447: wx.LANGUAGE_GUJARATI,

        # Nigeria (NG)
        # sub: SUBLANG_HAUSA_NIGERIA_LATIN primary: LANG_HAUSA
        0x0468: wx.LANGUAGE_HAUSA,

        # Israel (IL)
        # sub: SUBLANG_HEBREW_ISRAEL primary: LANG_HEBREW
        0x040D: wx.LANGUAGE_HEBREW,

        # India (IN)
        # sub: SUBLANG_HINDI_INDIA primary: LANG_HINDI
        0x0439: wx.LANGUAGE_HINDI,

        # Hungary (HU)
        # sub: SUBLANG_HUNGARIAN_HUNGARY primary: LANG_HUNGARIAN
        0x040E: wx.LANGUAGE_HUNGARIAN,

        # Iceland (IS)
        # sub: SUBLANG_ICELANDIC_ICELAND primary: LANG_ICELANDIC
        0x040F: wx.LANGUAGE_ICELANDIC,

        # Indonesia (ID)
        # sub: SUBLANG_INDONESIAN_INDONESIA primary: LANG_INDONESIAN
        0x0421: wx.LANGUAGE_INDONESIAN,

        # no x-ref wx.LANGUAGE_INTERLINGUA
        # no x-ref wx.LANGUAGE_INTERLINGUE

        # Canada (CA), Latin
        # sub: SUBLANG_INUKTITUT_CANADA_LATIN primary: LANG_INUKTITUT
        0x085D: wx.LANGUAGE_INUKTITUT,

        # no x-ref wx.LANGUAGE_INUPIAK

        # Ireland (IE)
        # sub: SUBLANG_IRISH_IRELAND primary: LANG_IRISH
        0x083C: wx.LANGUAGE_IRISH,

        # South Africa (ZA)
        # sub: SUBLANG_XHOSA_SOUTH_AFRICA primary: LANG_XHOSA
        0x0434: wx.LANGUAGE_XHOSA,

        # South Africa (ZA)
        # sub: SUBLANG_ZULU_SOUTH_AFRICA primary: LANG_ZULU
        0x0435: wx.LANGUAGE_ZULU,

        # Italy (IT)
        # sub: SUBLANG_ITALIAN primary: LANG_ITALIAN
        0x0410: wx.LANGUAGE_ITALIAN,

        # Switzerland (CH)
        # sub: SUBLANG_ITALIAN_SWISS primary: LANG_ITALIAN
        0x0810: wx.LANGUAGE_ITALIAN_SWISS,

        # Japan (JP)
        # sub: SUBLANG_JAPANESE_JAPAN primary: LANG_JAPANESE
        0x0411: wx.LANGUAGE_JAPANESE,

        # no x-ref wx.LANGUAGE_JAVANESE
        # no x-ref wx.LANGUAGE_KABYLE

        # India (IN)
        # sub: SUBLANG_KANNADA_INDIA primary: LANG_KANNADA
        0x044B: wx.LANGUAGE_KANNADA,

        # no x-ref wx.LANGUAGE_KASHMIRI

        # (reserved)
        # sub: SUBLANG_KASHMIRI_INDIA primary: LANG_KASHMIRI
        # ______: wx.LANGUAGE_KASHMIRI_INDIA,

        # Kazakhstan (KZ)
        # sub: SUBLANG_KAZAK_KAZAKHSTAN primary: LANG_KAZAK
        0x043F: wx.LANGUAGE_KAZAKH,

        # no x-ref wx.LANGUAGE_KERNEWEK

        # Rwanda (RW)
        # sub: SUBLANG_KINYARWANDA_RWANDA primary: LANG_KINYARWANDA
        0x0487: wx.LANGUAGE_KINYARWANDA,

        # no x-ref wx.LANGUAGE_KIRGHIZ
        # no x-ref wx.LANGUAGE_KIRUNDI

        # India (IN)
        # sub: SUBLANG_KONKANI_INDIA primary: LANG_KONKANI
        0x0457: wx.LANGUAGE_KONKANI,

        # Korea (KR)
        # sub: SUBLANG_KOREAN primary: LANG_KOREAN
        0x0412: wx.LANGUAGE_KOREAN,

        # no x-ref wx.LANGUAGE_LAOTHIAN

        # Latvia (LV)
        # sub: SUBLANG_LATVIAN_LATVIA primary: LANG_LATVIAN
        0x0426: wx.LANGUAGE_LATVIAN,

        # no x-ref wx.LANGUAGE_LINGALA

        # Lithuanian (LT); see note 5
        # sub: SUBLANG_LITHUANIAN_LITHUANIA primary: LANG_LITHUANIAN
        0x0427: wx.LANGUAGE_LITHUANIAN,

        # Macedonia (FYROM) (MK)
        # sub: SUBLANG_MACEDONIAN_MACEDONIA primary: LANG_MACEDONIAN
        0x042F: wx.LANGUAGE_MACEDONIAN,

        # Brunei Darassalam (BN)
        # sub: SUBLANG_MALAY_BRUNEI_DARUSSALAM primary: LANG_MALAY
        0x083E: wx.LANGUAGE_MALAY_BRUNEI_DARUSSALAM,

        # Malaysia (MY)
        # sub: SUBLANG_MALAY_MALAYSIA primary: LANG_MALAY
        0x043e: wx.LANGUAGE_MALAY_MALAYSIA,

        # no x-ref wx.LANGUAGE_MALAGASY

        # India (IN)
        # sub: SUBLANG_MALAYALAM_INDIA primary: LANG_MALAYALAM
        0x044C: wx.LANGUAGE_MALAYALAM,

        # Malta (MT)
        # sub: SUBLANG_MALTESE_MALTA primary: LANG_MALTESE
        0x043A: wx.LANGUAGE_MALTESE,

        # no x-ref wx.LANGUAGE_MANIPURI

        # New Zealand (NZ)
        # sub: SUBLANG_MAORI_NEW_ZEALAND primary: LANG_MAORI
        0x0481: wx.LANGUAGE_MAORI,

        # India (IN)
        # sub: SUBLANG_MARATHI_INDIA primary: LANG_MARATHI
        0x044E: wx.LANGUAGE_MARATHI,

        # no x-ref wx.LANGUAGE_MOLDAVIAN

        # Mongolia, Mong (MN)
        # sub: SUBLANG_MONGOLIAN_PRC primary: LANG_MONGOLIAN
        0x0850: wx.LANGUAGE_MONGOLIAN,

        # no x-ref wx.LANGUAGE_NAURU

        # Nepal (NP)
        # sub: SUBLANG_NEPALI_NEPAL primary: LANG_NEPALI
        0x0461: wx.LANGUAGE_NEPALI,

        # no x-ref wx.LANGUAGE_NEPALI_INDIA

        # Bokmål, Norway (NO)
        # sub: SUBLANG_NORWEGIAN_BOKMAL primary: LANG_NORWEGIAN
        0x0414: wx.LANGUAGE_NORWEGIAN_BOKMAL,

        # Nynorsk, Norway (NO)
        # sub: SUBLANG_NORWEGIAN_NYNORSK primary: LANG_NORWEGIAN
        0x0814: wx.LANGUAGE_NORWEGIAN_NYNORSK,

        # France (FR)
        # sub: SUBLANG_OCCITAN_FRANCE primary: LANG_OCCITAN
        0x0482: wx.LANGUAGE_OCCITAN,

        # India (IN)
        # sub: SUBLANG_ORIYA_INDIA primary: LANG_ORIYA
        0x0448: wx.LANGUAGE_ORIYA,

        # no x-ref wx.LANGUAGE_OROMO

        # Afghanistan (AF)
        # sub: SUBLANG_PASHTO_AFGHANISTAN primary: LANG_PASHTO
        0x0463: wx.LANGUAGE_PASHTO,

        # Poland (PL)
        # sub: SUBLANG_POLISH_POLAND primary: LANG_POLISH
        0x0415: wx.LANGUAGE_POLISH,

        # Brazil (BR)
        # sub: SUBLANG_PORTUGUESE_BRAZILIAN primary: LANG_PORTUGUESE
        0x0416: wx.LANGUAGE_PORTUGUESE_BRAZILIAN,

        # Portugal (PT); see note 7
        # sub: SUBLANG_PORTUGUESE primary: LANG_PORTUGUESE
        0x0816: wx.LANGUAGE_PORTUGUESE,

        # India, Gurmukhi script (IN)
        # sub: SUBLANG_PUNJABI_INDIA primary: LANG_PUNJABI
        0x0446: wx.LANGUAGE_PUNJABI,

        # Bolivia (BO)
        # sub: SUBLANG_QUECHUA_BOLIVIA primary: LANG_QUECHUA
        0x046B: wx.LANGUAGE_QUECHUA,

        # no x-ref wx.LANGUAGE_RHAETO_ROMANCE

        # Romania (RO)
        # sub: SUBLANG_ROMANIAN_ROMANIA primary: LANG_ROMANIAN
        0x0418: wx.LANGUAGE_ROMANIAN,

        # Russia (RU)
        # sub: SUBLANG_RUSSIAN_RUSSIA primary: LANG_RUSSIAN
        0x0419: wx.LANGUAGE_RUSSIAN,

        # no x-ref wx.LANGUAGE_RUSSIAN_UKRAINE

        # Inari, Finland (FI)
        # sub: SUBLANG_SAMI_INARI_FINLAND primary: LANG_SAMI
        0x243B: wx.LANGUAGE_SAMI,

        # no x-ref wx.LANGUAGE_SAMOAN
        # no x-ref wx.LANGUAGE_SANGHO

        # India (IN)
        # sub: SUBLANG_SANSKRIT_INDIA primary: LANG_SANSKRIT
        0x044F: wx.LANGUAGE_SANSKRIT,

        # no x-ref wx.LANGUAGE_SCOTS_GAELIC

        # Serbian (sr)
        # sub:  primary: LANG_SERBIAN
        0x1a:   wx.LANGUAGE_SERBIAN,

        # no x-ref wx.LANGUAGE_SERBO_CROATIAN

        # Serbia and Montenegro (former), Cyrillic (CS)
        # sub: SUBLANG_SERBIAN_CYRILLIC primary: LANG_SERBIAN
        0x0C1A: wx.LANGUAGE_SERBIAN_CYRILLIC,

        # Serbia and Montenegro (former), Latin (CS)
        # sub: SUBLANG_SERBIAN_LATIN primary: LANG_SERBIAN
        0x081A: wx.LANGUAGE_SERBIAN_LATIN,

        # no x-ref wx.LANGUAGE_SESOTHO
        # no x-ref wx.LANGUAGE_SETSWANA
        # no x-ref wx.LANGUAGE_SHONA

        # (reserved)
        # sub: primary: LANG_TSWANA
        0x59:   wx.LANGUAGE_SINDHI,

        # Sri Lanka (LK)
        # sub: SUBLANG_SINHALESE_SRI_LANKA primary: LANG_SINHALESE
        0x045B: wx.LANGUAGE_SINHALESE,

        # no x-ref wx.LANGUAGE_SISWATI

        # Slovakia (SK)
        # sub: SUBLANG_SLOVAK_SLOVAKIA primary: LANG_SLOVAK
        0x041B: wx.LANGUAGE_SLOVAK,

        # Slovenia (SI)
        # sub: SUBLANG_SLOVENIAN_SLOVENIA primary: LANG_SLOVENIAN
        0x0424: wx.LANGUAGE_SLOVENIAN,

        # no x-ref wx.LANGUAGE_SOMALI

        # Spain, Traditional Sort (ES)
        # sub: SUBLANG_SPANISH primary: LANG_SPANISH
        0x040A: wx.LANGUAGE_SPANISH,

        # Bolivia (BO)
        # sub: SUBLANG_SPANISH_BOLIVIA primary: LANG_SPANISH
        0x400A: wx.LANGUAGE_SPANISH_BOLIVIA,

        # Chile (CL)
        # sub: SUBLANG_SPANISH_CHILE primary: LANG_SPANISH
        0x340A: wx.LANGUAGE_SPANISH_CHILE,

        # Colombia (CO)
        # sub: SUBLANG_SPANISH_COLOMBIA primary: LANG_SPANISH
        0x240A: wx.LANGUAGE_SPANISH_COLOMBIA,

        # Costa Rica (CR)
        # sub: SUBLANG_SPANISH_COSTA_RICA primary: LANG_SPANISH
        0x140A: wx.LANGUAGE_SPANISH_COSTA_RICA,

        # Dominican Republic (DO)
        # sub: SUBLANG_SPANISH_DOMINICAN_REPUBLIC primary: LANG_SPANISH
        0x1C0A: wx.LANGUAGE_SPANISH_DOMINICAN_REPUBLIC,

        # Ecuador (EC)
        # sub: SUBLANG_SPANISH_ECUADOR primary: LANG_SPANISH
        0x300A: wx.LANGUAGE_SPANISH_ECUADOR,

        # El Salvador (SV)
        # sub: SUBLANG_SPANISH_EL_SALVADOR primary: LANG_SPANISH
        0x440A: wx.LANGUAGE_SPANISH_EL_SALVADOR,

        # Guatemala (GT)
        # sub: SUBLANG_SPANISH_GUATEMALA primary: LANG_SPANISH
        0x100A: wx.LANGUAGE_SPANISH_GUATEMALA,

        # Honduras (HN)
        # sub: SUBLANG_SPANISH_HONDURAS primary: LANG_SPANISH
        0x480A: wx.LANGUAGE_SPANISH_HONDURAS,

        # Mexico (MX)
        # sub: SUBLANG_SPANISH_MEXICAN primary: LANG_SPANISH
        0x080A: wx.LANGUAGE_SPANISH_MEXICAN,

        # Nicaragua (NI)
        # sub: SUBLANG_SPANISH_NICARAGUA primary: LANG_SPANISH
        0x4C0A: wx.LANGUAGE_SPANISH_NICARAGUA,

        # Panama (PA)
        # sub: SUBLANG_SPANISH_PANAMA primary: LANG_SPANISH
        0x180A: wx.LANGUAGE_SPANISH_PANAMA,

        # Paraguay (PY)
        # sub: SUBLANG_SPANISH_PARAGUAY primary: LANG_SPANISH
        0x3C0A: wx.LANGUAGE_SPANISH_PARAGUAY,

        # Peru (PE)
        # sub: SUBLANG_SPANISH_PERU primary: LANG_SPANISH
        0x280A: wx.LANGUAGE_SPANISH_PERU,

        # Puerto Rico (PR)
        # sub: SUBLANG_SPANISH_PUERTO_RICO primary: LANG_SPANISH
        0x500A: wx.LANGUAGE_SPANISH_PUERTO_RICO,

        # Spain, Modern Sort (ES)
        # sub: SUBLANG_SPANISH_MODERN primary: LANG_SPANISH
        0x0C0A: wx.LANGUAGE_SPANISH_MODERN,

        # Argentina (AR)
        # sub: SUBLANG_SPANISH_ARGENTINA primary: LANG_SPANISH
        0x2C0A: wx.LANGUAGE_SPANISH_ARGENTINA,

        # United States (US)
        # sub: SUBLANG_SPANISH_US primary: LANG_SPANISH
        0x540A: wx.LANGUAGE_SPANISH_US,

        # Uruguay (UY)
        # sub: SUBLANG_SPANISH_URUGUAY primary: LANG_SPANISH
        0x380A: wx.LANGUAGE_SPANISH_URUGUAY,

        # Venezuela (VE)
        # sub: SUBLANG_SPANISH_VENEZUELA primary: LANG_SPANISH
        0x200A: wx.LANGUAGE_SPANISH_VENEZUELA,

        # no x-ref wx.LANGUAGE_SUNDANESE

        # Kenya (KE)
        # sub: SUBLANG_SWAHILI primary: LANG_SWAHILI
        0x0441: wx.LANGUAGE_SWAHILI,

        # Finland (FI)
        # sub: SUBLANG_SWEDISH_FINLAND primary: LANG_SWEDISH
        0x081D: wx.LANGUAGE_SWEDISH_FINLAND,

        # Sweden (SE); see note 8
        # sub: SUBLANG_SWEDISH primary: LANG_SWEDISH
        0x041D: wx.LANGUAGE_SWEDISH,

        # no x-ref wx.LANGUAGE_TAGALOG

        # Tajikistan, Cyrillic (TJ)
        # sub: SUBLANG_TAJIK_TAJIKISTAN primary: LANG_TAJIK
        0x0428: wx.LANGUAGE_TAJIK,

        # India (IN)
        # sub: SUBLANG_TAMIL_INDIA primary: LANG_TAMIL
        0x0449: wx.LANGUAGE_TAMIL,

        # Russia (RU)
        # sub: SUBLANG_TATAR_RUSSIA primary: LANG_TATAR
        0x0444: wx.LANGUAGE_TATAR,

        # India (IN)
        # sub: SUBLANG_TELUGU_INDIA primary: LANG_TELUGU
        0x044A: wx.LANGUAGE_TELUGU,

        # Thailand (TH)
        # sub: SUBLANG_THAI_THAILAND primary: LANG_THAI
        0x041E: wx.LANGUAGE_THAI,

        # PRC (CN)
        # sub: SUBLANG_TIBETAN_PRC primary: LANG_TIBETAN
        0x0451: wx.LANGUAGE_TIBETAN,

        # Eritrea (ER)
        # sub: SUBLANG_TIGRINYA_ERITREA primary: LANG_TIGRINYA
        0x0873: wx.LANGUAGE_TIGRINYA,

        # no x-ref wx.LANGUAGE_TONGA
        # no x-ref wx.LANGUAGE_TSONGA

        # Turkey (TR)
        # sub: SUBLANG_TURKISH_TURKEY primary: LANG_TURKISH
        0x041F: wx.LANGUAGE_TURKISH,

        # Turkmenistan (TM)
        # sub: SUBLANG_TURKMEN_TURKMENISTAN primary: LANG_TURKMEN
        0x0442: wx.LANGUAGE_TURKMEN,

        # no x-ref wx.LANGUAGE_TWI

        # Ukraine (UA)
        # sub: SUBLANG_UKRAINIAN_UKRAINE primary: LANG_UKRAINIAN
        0x0422: wx.LANGUAGE_UKRAINIAN,

        # (reserved)
        # sub: SUBLANG_URDU_INDIA primary: LANG_URDU
        0x0820: wx.LANGUAGE_URDU_INDIA,

        # Urdu (ur)
        # sub: primary: LANG_URDU
        0x20:   wx.LANGUAGE_URDU,

        # Pakistan (PK)
        # sub: SUBLANG_URDU_PAKISTAN primary: LANG_URDU
        0x0420: wx.LANGUAGE_URDU_PAKISTAN,

        # PRC (CN)
        # sub: SUBLANG_UIGHUR_PRC primary: LANG_UIGHUR
        0x0480: wx.LANGUAGE_UIGHUR,

        # Uzbek (uz)
        # sub: primary: LANG_UZBEK
        0x43:   wx.LANGUAGE_UZBEK,

        # Uzbekistan, Cyrillic (UZ)
        # sub: SUBLANG_UZBEK_CYRILLIC primary: LANG_UZBEK
        0x0843: wx.LANGUAGE_UZBEK_CYRILLIC,

        # Uzbekistan, Latin (UZ)
        # sub: SUBLANG_UZBEK_LATIN primary: LANG_UZBEK
        0x0443: wx.LANGUAGE_UZBEK_LATIN,

        # Valencia (ES-Valencia)
        # sub: SUBLANG_VALENCIAN_VALENCIA primary: LANG_VALENCIAN
        0x0803: wx.LANGUAGE_VALENCIAN,

        # Vietnam (VN)
        # sub: SUBLANG_VIETNAMESE_VIETNAM primary: LANG_VIETNAMESE
        0x042A: wx.LANGUAGE_VIETNAMESE,

        # no x-ref wx.LANGUAGE_VOLAPUK

        # United Kingdom (GB)
        # sub: SUBLANG_WELSH_UNITED_KINGDOM primary: LANG_WELSH
        0x0452: wx.LANGUAGE_WELSH,

        # Senegal (SN)
        # sub: SUBLANG_WOLOF_SENEGAL primary: LANG_WOLOF
        0x0488: wx.LANGUAGE_WOLOF,

        # no x-ref wx.LANGUAGE_YIDDISH

        # Nigeria (NG)
        # sub: SUBLANG_YORUBA_NIGERIA primary: LANG_YORUBA
        0x046A: wx.LANGUAGE_YORUBA,

        # no x-ref wx.LANGUAGE_ZHUANG
    }
except ImportError:
    wx = None
    LCID_TO_WX = {}

PY3 = sys.version_info[0] > 2

BASE_PATH = os.path.abspath(os.path.dirname(__file__))


kernel32 = ctypes.windll.Kernel32

# LCID LocaleNameToLCID(
#   LPCWSTR lpName,
#   DWORD   dwFlags
# );
_LocaleNameToLCID = kernel32.LocaleNameToLCID
_LocaleNameToLCID.restype = LCID

# int LCIDToLocaleName(
#   LCID   Locale,
#   LPWSTR lpName,
#   int    cchName,
#   DWORD  dwFlags
# );
_LCIDToLocaleName = kernel32.LCIDToLocaleName
_LCIDToLocaleName.restype = INT

# LANGID GetUserDefaultUILanguage();
GetUserDefaultUILanguage = kernel32.GetUserDefaultUILanguage


# int GetUserDefaultLocaleName(
#   LPWSTR lpLocaleName,
#   int    cchLocaleName
# );

GetUserDefaultLocaleName = kernel32.GetUserDefaultLocaleName
GetUserDefaultLocaleName.restype = INT

LOCALE_NAME_MAX_LENGTH = 85
LOCALE_ALLOW_NEUTRAL_NAMES = 0x08000000
DEFAULT_USER_LANGUAGE = 'en-US'


# noinspection PyTypeChecker,PyCallingNonCallable
def get_windows_user_language():
    lp_locale_name = (WCHAR * LOCALE_NAME_MAX_LENGTH)()
    cch_locale_name = INT(LOCALE_NAME_MAX_LENGTH)

    if not GetUserDefaultLocaleName(
        ctypes.byref(lp_locale_name),
        cch_locale_name
    ):
        raise ctypes.WinError()

    lp_locale_name = lp_locale_name.value

    for locale in locales:
        for lng in locale.languages:
            if lng.iso_code == lp_locale_name:
                return lng

    lcid = GetUserDefaultUILanguage()

    for locale in locales:
        for lng in locale.languages:
            if lng.lcid == lcid:
                return lng

    default_language, default_locale = DEFAULT_USER_LANGUAGE.rsplit('-', 1)

    for locale in locales:
        if not locale == default_locale:
            continue
        for lang in locale.languages:
            if lang == default_language:
                return lang


def locale_name_to_lcid(locale_name):

    if isinstance(locale_name, str):
        if PY3:
            locale_name = locale_name.encode('utf-8')
        else:
            # noinspection PyUnresolvedReferences
            locale_name = unicode(locale_name)

    res = _LocaleNameToLCID(locale_name, DWORD(0))
    if res == 0:
        return None
    return res


class Language(object):
    ISO639_1 = None
    ISO639_2 = None
    ISO639_3 = None
    english_name = ''
    native_name = u''
    _lcid = None
    _lang_id = None

    def __init__(self, locale_name, lcid=None):
        if lcid is not None:
            self._lcid = lcid
        self.locale_name = locale_name
        self.locale = None
        self._iso_code = None

    # noinspection PyUnresolvedReferences
    def __eq__(self, other):
        if isinstance(other, Language):
            other_iso = other.iso_code
            self_iso = self.iso_code

            return (
                other_iso is not None and
                self_iso is not None and
                other_iso == self_iso
            )
        elif isinstance(other, int):
            return other == self.lcid

        else:
            if PY3:
                if isinstance(other, bytes):
                    other = other.decode('utf-8')

                if isinstance(other, str):
                    self_iso = self.iso_code

                    return (
                        self_iso is not None and (
                            other == self_iso or
                            self_iso.startswith(other)
                        )
                    )
            elif isinstance(other, (str, unicode)):
                self_iso = self.iso_code

                return (
                    self_iso is not None and (
                        other == self_iso or
                        self_iso.startswith(other)
                    )
                )

        return False

    @property
    def label(self):
        return self.locale_name

    @property
    def iso_code(self):
        if self._iso_code is None and self.ISO639_3 is not None:
            iso_code = self.ISO639_3 + '-' + self.locale.locale_iso_code
            if locale_name_to_lcid(iso_code) is not None:
                self._iso_code = iso_code

        if self._iso_code is None and self.ISO639_2 is not None:
            iso_code = self.ISO639_2 + '-' + self.locale.locale_iso_code
            if locale_name_to_lcid(iso_code) is not None:
                self._iso_code = iso_code

        if self._iso_code is None and self.ISO639_1 is not None:
            iso_code = self.ISO639_1 + '-' + self.locale.locale_iso_code
            if locale_name_to_lcid(iso_code) is not None:
                self._iso_code = iso_code

        return self._iso_code

    @property
    def lang_iso_code(self):
        iso_code = self.iso_code
        if iso_code is not None:
            if self.ISO639_3 is not None and self.ISO639_3 in iso_code:
                return self.ISO639_3
            if self.ISO639_2 is not None and self.ISO639_2 in iso_code:
                return self.ISO639_2
            if self.ISO639_1 is not None and self.ISO639_1 in iso_code:
                return self.ISO639_1

    @property
    def lcid(self):
        if self._lcid is None:
            lcid = locale_name_to_lcid(self.iso_code)
            self._lcid = lcid

        return self._lcid

    @property
    def wx_code(self):
        lcid = self.lcid
        if lcid is None:
            return

        if lcid in LCID_TO_WX:
            return LCID_TO_WX[lcid]

    def set_locale(self):
        iso_code = self.iso_code

        if iso_code is None:
            return

        locale = (
            'LC_COLLATE={0};'
            'LC_CTYPE={0};'
            'LC_MONETARY={0};'
            'LC_NUMERIC={0};'
            'LC_TIME={0}'
        ).format(self.iso_code)

        _locale.setlocale(_locale.LC_ALL, locale)

    def set_wx_locale(self):
        if wx is not None:
            wx_code = self.wx_code
            if wx_code is None:
                return

            app = wx.GetApp()
            if app is None:
                return

            app.locale = wx.Locale(wx_code)


class Locales(object):
    def __init__(self):
        self._locales = []

    def append(self, locale):
        for lcl in self:
            if lcl == locale:
                break
        else:
            self._locales += [locale]

    def __iter__(self):
        for locale in self._locales:
            yield locale

    def __getitem__(self, item):
        for locale in self:
            if locale == item:
                return locale

        raise KeyError(item)

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        for locale in self:
            if locale == item:
                return locale

        raise AttributeError(item)


locales = Locales()


class LocaleMeta(type):

    def __new__(mcs, name, bases, dct):
        locale = type.__new__(mcs, name, bases, dct)
        instance = locale()
        for lang in instance.languages[:]:
            if lang.iso_code is None:
                instance.languages.remove(lang)

        if instance.languages:
            locales.append(instance)
        return locale


class Locale(object):
    __metaclass__ = LocaleMeta

    _iso_code = ''
    english_name = ''
    _flag = ''
    languages = []

    def __init__(self):
        for language in self.languages:
            language.locale = self

    def __iter__(self):
        for language in self.languages:
            yield language

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        if item in Locale.__dict__:
            if hasattr(Locale.__dict__[item], 'fget'):
                return Locale.__dict__[item].fget(self)

        for language in self:
            if language == item:
                return language

        raise AttributeError(item)

    def __getitem__(self, item):
        for language in self:
            if language == item:
                return language

        raise KeyError(item)

    # noinspection PyUnresolvedReferences
    def __eq__(self, other):
        if isinstance(other, Locale):
            return other.locale_iso_code == self.locale_iso_code

        if PY3:
            if isinstance(other, bytes):
                other = other.decode('utf-8')

            if isinstance(other, str):
                return other == self.locale_iso_code

        elif isinstance(other, (str, unicode)):
            return other == self.locale_iso_code

        return False

    @property
    def locale_iso_code(self):
        return self._iso_code

    @property
    def flag(self):
        if self._flag:
            with open(os.path.join(BASE_PATH, self._flag), 'wb') as f:
                return f.read()


class Afar(Language):
    ISO639_1 = 'aa'
    ISO639_2 = 'aar'
    english_name = 'Afar'
    native_name = u'Qafár af'
    _lang_id = 0x1000


class Afrikaans(Language):
    ISO639_1 = 'af'
    ISO639_2 = 'afr'
    english_name = 'Afrikaans'
    native_name = u'Afrikaans'
    _lang_id = 0x0036


class Aghem(Language):
    ISO639_2 = 'agq'
    english_name = 'Aghem'
    native_name = u'Aghem'
    _lang_id = 0x1000


class Akan(Language):
    ISO639_1 = 'ak'
    ISO639_2 = 'aka'
    english_name = 'Akan'
    native_name = u'Akan'
    _lang_id = 0x1000


class Albanian(Language):
    ISO639_1 = 'sq'
    ISO639_2 = 'alb'
    english_name = 'Albanian'
    native_name = u'Shqip'
    _lang_id = 0x001C


class SwissGerman(Language):
    ISO639_2 = 'gsw'
    english_name = 'Swiss German'
    nnative_name = u'Schwiizerdütsch'
    _lang_id = 0x0084


class Amharic(Language):
    ISO639_1 = 'am'
    ISO639_2 = 'amh'
    english_name = 'Amharic'
    native_name = u'አማርኛ'
    _lang_id = 0x005E


class Arabic(Language):
    ISO639_1 = 'ar'
    ISO639_2 = 'ara'
    english_name = 'Arabic'
    native_name = u'العَرَبِيَّة'
    _lang_id = 0x0001


class Armenian(Language):
    ISO639_1 = 'hy'
    ISO639_2 = 'arm'
    ISO639_3 = 'hye'
    english_name = 'Armenian'
    native_name = u' Հայերէն'
    _lang_id = 0x002B


class Assamese(Language):
    ISO639_1 = 'as'
    ISO639_2 = 'asm'
    english_name = 'Assamese'
    native_name = u'অসমীয়া'
    _lang_id = 0x004D


class Asturian(Language):
    ISO639_2 = 'ast'
    english_name = 'Asturian'
    native_name = u'Asturianu'
    _lang_id = 0x1000


class Asu(Language):
    ISO639_2 = 'asa'
    english_name = 'Asu'
    native_name = u'Asu'
    _lang_id = 0x1000


class Aymara(Language):
    ISO639_1 = 'ay'
    ISO639_2 = 'aym'
    english_name = 'Aymara'
    native_name = u'Aymar aru'


class AzerbaijaniCyrillic(Language):
    ISO639_3 = 'az-Cyrl'
    english_name = 'Azerbaijani'
    native_name = u'Азәрбајҹан дили'
    _lang_id = 0x742C


class AzerbaijaniLatin(Language):
    ISO639_3 = 'az-Latn'
    english_name = 'Azerbaijani'
    native_name = u'Azərbaycan dili'
    _lang_id = 0x782C


class Azerbaijani(Language):
    ISO639_1 = 'az'
    ISO639_2 = 'aze'
    english_name = 'Azerbaijani'
    native_name = u'آذربایجان دیلی'
    _lang_id = 0x002C


class Bafia(Language):
    ISO639_2 = 'ksf'
    english_name = 'Bafia'
    native_name = u'Bafia'
    _lang_id = 0x1000


class Bamanankan(Language):
    ISO639_1 = 'bm'
    english_name = 'Bamanankan'
    native_name = u'Bamanankan'
    _lang_id = 0x1000


class BamanankanLatin(Language):
    ISO639_1 = 'bm'
    ISO639_3 = 'bm-Latn'
    english_name = 'Bamanankan (Latin)'
    native_name = u'Bamanankan (Latin)'
    _lang_id = 0x1000


class Basaa(Language):
    ISO639_2 = 'bas'
    english_name = 'Basaa'
    native_name = u'Basaa'
    _lang_id = 0x1000


class Bashkir(Language):
    ISO639_1 = 'ba'
    english_name = 'Bashkir'
    native_name = u' Башҡорт теле'
    _lang_id = 0x006D


class Basque(Language):
    ISO639_1 = 'eu'
    ISO639_2 = 'baq'
    english_name = 'Basque'
    native_name = u'euskara'
    _lang_id = 0x002D


class Bavarian(Language):
    ISO639_2 = 'bar'
    english_name = 'Bavarian'
    native_name = u'bairisch'


class Belarusian(Language):
    ISO639_1 = 'be'
    ISO639_2 = 'bel'
    english_name = 'Belarusian'
    native_name = u'Беларуская мова'
    _lang_id = 0x0023


class Bemba(Language):
    ISO639_2 = 'bem'
    english_name = 'Bemba'
    native_name = u'Chibemba'
    _lang_id = 0x1000


class Bena(Language):
    ISO639_2 = 'bez'
    english_name = 'Bena'
    native_name = u'Bena'
    _lang_id = 0x1000


class Blin(Language):
    ISO639_2 = 'byn'
    english_name = 'Blin'
    native_name = u'ብሊን'
    _lang_id = 0x1000


class Bodo(Language):
    ISO639_1 = 'brx'
    english_name = 'Bodo'
    native_name = u'Bodo'
    _lang_id = 0x1000


class Bosnian(Language):
    ISO639_1 = 'bs'
    ISO639_2 = 'bos'
    english_name = 'Bosnian'
    native_name = u'босански'
    _lang_id = 0x781A


class BosnianCyrillic(Language):
    ISO639_1 = 'bs'
    ISO639_2 = 'bos'
    ISO639_3 = 'bs-Cyrl'
    english_name = 'Bosnian (Cyrillic)'
    native_name = u'беларуская мова'
    _lang_id = 0x641A


class BosnianLatin(Language):
    ISO639_1 = 'bs'
    ISO639_2 = 'bos'
    ISO639_3 = 'bs-Latn'
    english_name = 'Bosnian (Latin)'
    native_name = u'bosanski'
    _lang_id = 0x681A


class Breton(Language):
    ISO639_1 = 'br'
    ISO639_2 = 'bre'
    english_name = 'Breton'
    native_name = u'Brezhoneg'
    _lang_id = 0x007E


class Bulgarian(Language):
    ISO639_1 = 'bg'
    ISO639_2 = 'bul'
    english_name = 'Bulgarian'
    native_name = u'български език'
    _lang_id = 0x0002


class Bislama(Language):
    ISO639_1 = 'bi'
    ISO639_2 = 'bis'
    english_name = 'Bislama'
    native_name = u'Bislama'


class Bengali(Language):
    ISO639_1 = 'bn'
    ISO639_2 = 'ben'
    english_name = 'Bengali'
    native_name = u'বাংলা'
    _lang_id = 0x0045


class Burmese(Language):
    ISO639_1 = 'my'
    ISO639_2 = 'bur'
    english_name = 'Burmese'
    native_name = u'မြန်မာစာ'
    _lang_id = 0x0055


class Catalan(Language):
    ISO639_1 = 'ca'
    ISO639_2 = 'cat'
    english_name = 'Catalan'
    native_name = u'català'
    _lang_id = 0x0003


class CentralAtlasTamazightLatin(Language):
    ISO639_3 = 'tzm-Latn-MA'
    english_name = 'Central Atlas Tamazight (Latin)'
    native_name = u'Central Atlas Tamazight (Latin)'
    _lang_id = 0x1000


class CentralKurdish(Language):
    ISO639_1 = 'ku'
    ISO639_2 = 'kur'
    english_name = 'Central Kurdish'
    native_name = u'Kurdî'
    _lang_id = 0x0092


class CentralKurdishArab(Language):
    ISO639_1 = 'ku'
    ISO639_2 = 'kur'
    ISO639_3 = 'ku-Arab'
    english_name = 'Central Kurdish (Arab)'
    native_name = u'کوردی (Arab)'
    _lang_id = 0x7c92


class Chamorro(Language):
    ISO639_1 = 'ch'
    ISO639_2 = 'cha'
    english_name = 'Chamorro'
    native_language = u'Finu\' Chamoru'


class Chechen(Language):
    ISO639_1 = 'ce'
    ISO639_2 = 'che'
    english_name = 'Chechen'
    native_name = u'Нохчийн мотт'
    _lang_id = 0x1000


class Cherokee(Language):
    ISO639_2 = 'chr'
    english_name = 'Cherokee'
    native_name = u'ᏣᎳᎩ ᎦᏬᏂᎯᏍᏗ'
    _lang_id = 0x005C


class Chiga(Language):
    ISO639_2 = 'cgg'
    english_name = 'Chiga'
    native_name = u'Chiga'
    _lang_id = 0x1000


class ChineseSimplified(Language):
    ISO639_1 = 'zh'
    english_name = 'Chinese (Simplified)'
    native_name = u'中文'
    _lang_id = 0x7804


class ChineseSimplifiedHans(Language):
    ISO639_2 = 'chi'
    ISO639_3 = 'zh-Hans'
    english_name = 'Chinese (Simplified)'
    native_name = u'汉语'
    _lang_id = 0x0004


class ChineseTraditional(Language):
    ISO639_2 = 'zho'
    ISO639_3 = 'zh-Hant'
    english_name = 'Chinese (Traditional)'
    native_name = u'漢語'
    _lang_id = 0x7C04


class ChurchSlavic(Language):
    ISO639_1 = 'cu'
    ISO639_2 = 'chu'
    english_name = 'Church Slavic'
    native_name = u'Славе́нскїй ѧ҆зы́къ'
    _lang_id = 0x1000


class CongoSwahili(Language):
    ISO639_2 = 'swc'
    english_name = 'Congo Swahili'
    native_name = u'Congo Swahili'
    _lang_id = 0x1000


class Cornish(Language):
    ISO639_1 = 'kw'
    ISO639_2 = 'cor'
    english_name = 'Cornish'
    native_name = u'Kernowek'
    _lang_id = 0x1000


class Corsican(Language):
    ISO639_1 = 'co'
    ISO639_2 = 'cos'
    english_name = 'Corsican'
    native_name = u'Corsu'
    _lang_id = 0x0083


class CroatianLatin(Language):
    ISO639_1 = 'hr'
    ISO639_2 = 'hrv'
    english_name = 'Croatian (Latin)'
    native_name = u'hrvatski'
    _lang_id = 0x001A


class Croatian1(Language):
    ISO639_1 = 'bs'
    english_name = 'Croatian (?)'
    native_name = u'Croatian (?)'
    _lang_id = 0x001A


class Croatian2(Language):
    ISO639_1 = 'sr'
    english_name = 'Croatian (?)'
    native_name = u'Croatian (?)'
    _lang_id = 0x001A


class Czech(Language):
    ISO639_1 = 'cs'
    ISO639_2 = 'cze'
    english_name = 'Czech'
    native_name = u'čeština'
    _lang_id = 0x0005


class Danish(Language):
    ISO639_1 = 'da'
    ISO639_2 = 'dan'
    english_name = 'Danish'
    native_name = u'dansk'
    _lang_id = 0x0006


class Dari(Language):
    ISO639_1 = 'fa'
    ISO639_2 = 'per'
    english_name = 'Dari'
    native_name = u'درى'
    _lang_id = 0x008C


class Divehi(Language): # Dhivehi
    ISO639_1 = 'dv'
    ISO639_2 = 'div'
    english_name = 'Divehi'
    native_name = u'ދިވެހިބަސް'
    _lang_id = 0x0065


class Duala(Language):
    ISO639_2 = 'dua'
    english_name = 'Duala'
    native_name = u'Duala'
    _lang_id = 0x1000


class Dutch(Language):
    ISO639_1 = 'nl'
    ISO639_2 = 'dut'
    english_name = 'Dutch'
    native_name = u'Nederlands'
    _lang_id = 0x0013


class Dzongkha(Language):
    ISO639_1 = 'dz'
    ISO639_2 = 'dzo'
    english_name = 'Dzongkha'
    native_name = u'རྫོང་ཁ་'
    _lang_id = 0x1000


class Embu(Language):
    ISO639_2 = 'ebu'
    english_name = 'Embu'
    native_name = u'Embu'
    _lang_id = 0x1000


class English(Language):
    ISO639_1 = 'en'
    ISO639_2 = 'eng'
    english_name = 'English'
    native_name = u'English'
    _lang_id = 0x0009


class Esperanto(Language):
    ISO639_1 = 'eo'
    ISO639_2 = 'epo'
    english_name = 'Esperanto'
    native_name = u'Esperanto'
    _lang_id = 0x1000


class Estonian(Language):
    ISO639_1 = 'et'
    ISO639_2 = 'est'
    english_name = 'Estonian'
    native_name = u'eesti keel'
    _lang_id = 0x0025


class Ewe(Language):
    ISO639_1 = 'ee'
    ISO639_2 = 'ewe'
    english_name = 'Ewe'
    native_name = u'Èʋegbe'
    _lang_id = 0x1000


class Ewondo(Language):
    ISO639_2 = 'ewo'
    english_name = 'Ewondo'
    native_name = u'Ewondo'
    _lang_id = 0x1000


class Faroese(Language):
    ISO639_1 = 'fo'
    ISO639_2 = 'fao'
    english_name = 'Faroese'
    native_name = u'føroyskt'
    _lang_id = 0x0038


class Filipino(Language):
    ISO639_2 = 'fil'
    english_name = 'Filipino'
    native_name = u'Filipino'
    _lang_id = 0x0064


class Finnish(Language):
    ISO639_1 = 'fi'
    ISO639_2 = 'fin'
    english_name = 'Finnish'
    native_name = u'suomen kieli'
    _lang_id = 0x000B


class French(Language):
    ISO639_1 = 'fr'
    ISO639_2 = 'fre'
    english_name = 'French'
    native_name = u'français'
    _lang_id = 0x000C


class Frisian(Language):
    ISO639_1 = 'fy'
    ISO639_2 = 'fry'
    english_name = 'Frisian'
    native_name = u'Frysk'
    _lang_id = 0x0062


class Friulian(Language):
    ISO639_2 = 'fur'
    english_name = 'Friulian'
    native_name = u'Friulian'
    _lang_id = 0x1000


class Fulah(Language):
    ISO639_1 = 'ff'
    ISO639_2 = 'ful'
    english_name = 'Fulah'
    native_name = u'Fulfulde'
    _lang_id = 0x0067


class FulahLatin(Language):
    ISO639_3 = 'ff-Latn'
    english_name = 'Fulah (Latin)'
    native_name = u'Pular'
    _lang_id = 0x7C67


class Galician(Language):
    ISO639_1 = 'gl'
    ISO639_2 = 'glg'
    english_name = 'Galician'
    native_name = u'galego'
    _lang_id = 0x1000


class Ganda(Language):
    ISO639_1 = 'lg'
    ISO639_2 = 'lug'
    english_name = 'Ganda'
    native_name = u'Luganda'
    _lang_id = 0x1000


class Georgian(Language):
    ISO639_1 = 'ka'
    ISO639_2 = 'geo'
    english_name = 'Georgian'
    native_name = u'ქართული'
    _lang_id = 0x0037


class German(Language):
    ISO639_1 = 'de'
    ISO639_2 = 'ger'
    english_name = 'German'
    native_name = u'Deutsch'
    _lang_id = 0x0007


class Greek(Language):
    ISO639_1 = 'el'
    ISO639_2 = 'gre'
    english_name = 'Greek'
    native_name = u'Νέα Ελληνικά'
    _lang_id = 0x0008


class Guarani(Language):
    ISO639_1 = 'gn'
    ISO639_2 = 'grn'
    english_name = 'Guarani'
    native_name = u'Avañe\'ẽ'
    _lang_id = 0x0074


class Gujarati(Language):
    ISO639_1 = 'gu'
    ISO639_2 = 'guj'
    english_name = 'Gujarati'
    native_name = u'ગુજરાતી'


class Gusii(Language):
    ISO639_2 = 'guz'
    english_name = 'Gusii'
    native_name = u'Gusii'
    _lang_id = 0x1000


class HaitianCreole(Language):
    ISO639_1 = 'ht'
    ISO639_2 = 'hat'
    english_name = 'Haitian Creole'
    native_name = u'kreyòl ayisyen'


class Hausa(Language):
    ISO639_1 = 'ha'
    ISO639_2 = 'hau'
    english_name = 'Hausa'
    native_name = u'هَرْشَن'
    _lang_id = 0x0068


class HausaLatin(Language):
    ISO639_1 = 'ha'
    ISO639_2 = 'hau'
    ISO639_3 = 'ha-Latn'
    english_name = 'Hausa (Latin)'
    native_name = u'Harshen'
    _lang_id = 0x7C68


class Hawaiian(Language):
    ISO639_2 = 'haw'
    english_name = 'Hawaiian'
    native_name = u'ʻŌlelo Hawaiʻi'
    _lang_id = 0x0075


class Hebrew(Language):
    ISO639_1 = 'he'
    ISO639_2 = 'heb'
    english_name = 'Hebrew'
    native_name = u'עברית'
    _lang_id = 0x000D


class Hindi(Language):
    ISO639_1 = 'hi'
    ISO639_2 = 'hin'
    english_name = 'Hindi'
    native_name = u'हिन्दी'
    _lang_id = 0x0039


class HiriMotu(Language):
    ISO639_1 = 'ho'
    ISO639_2 = 'hmo'
    english_name = 'Hiri Motu'
    native_name = u'Hiri Motu'


class Hungarian(Language):
    ISO639_1 = 'hu'
    ISO639_2 = 'hun'
    english_name = 'Hungarian'
    native_name = u'magyar nyelv'
    _lang_id = 0x000E


class Icelandic(Language):
    ISO639_1 = 'is'
    ISO639_2 = 'ice'
    english_name = 'Icelandic'
    native_name = u'íslenska'
    _lang_id = 0x000F


class Igbo(Language):
    ISO639_1 = 'ig'
    ISO639_2 = 'ibo'
    english_name = 'Igbo'
    native_name = u'Asụsụ Igbo'
    _lang_id = 0x0070


class Indonesian(Language):
    ISO639_1 = 'id'
    ISO639_2 = 'ind'
    english_name = 'Indonesian'
    natiive_name = u'bahasa Indonesia'
    _lang_id = 0x0021


class Interlingua(Language):
    ISO639_1 = 'ia'
    english_name = 'Interlingua'
    native_name = u'Interlingua'
    _lang_id = 0x1000


class Inuktitut(Language):
    ISO639_1 = 'iu'
    ISO639_2 = 'iku'
    english_name = 'Inuktitut'
    native_name = u'ᐃᓄᒃᑎᑐᑦ'
    _lang_id = 0x005D


class InuktitutLatin(Language):
    ISO639_3 = 'iu-Latn'
    english_name = 'Inuktitut (Latin)'
    native_name = u'Inuktitut (Latin)'
    _lang_id = 0x7C5D


class InuktitutSyllabics(Language):
    ISO639_3 = 'iu-Cans'
    english_name = 'Inuktitut (Syllabics)'
    native_name = u'Inuktitut (Syllabics)'
    _lang_id = 0x785D


class Irish(Language):
    ISO639_1 = 'ga'
    ISO639_2 = 'gle'
    english_name = 'Irish'
    native_name = u'Gaeilge'
    _lang_id = 0x003C


class Italian(Language):
    ISO639_1 = 'it'
    ISO639_2 = 'ita'
    english_name = 'Italian'
    native_name = u'italiano'
    _lang_id = 0x0010


class Japanese(Language):
    ISO639_1 = 'ja'
    ISO639_2 = 'jpn'
    english_name = 'Japanese'
    native_name = u'日本語'
    _lang_id = 0x0011


class Javanese(Language):
    ISO639_1 = 'jv'
    ISO639_2 = 'jav'
    english_name = 'Javanese'
    native_name = u'ꦧꦱꦗꦮ'
    _lang_id = 0x1000


class JavaneseLatin(Language):
    ISO639_3 = 'jv-Latn'
    english_name = 'Javanese (Latin)'
    native_name = u'Javanese (Latin)'
    _lang_id = 0x1000


class JolaFonyi(Language):
    ISO639_2 = 'dyo'
    english_name = 'Jola-Fonyi'
    native_name = u'Jola-Fonyi'
    _lang_id = 0x1000


class Kabuverdianu(Language):
    ISO639_2 = 'kea'
    english_name = 'Kabuverdianu'
    native_name = u'Kabuverdianu'
    _lang_id = 0x1000


class Kabyle(Language):
    ISO639_2 = 'kab'
    english_name = 'Kabyle'
    native_name = u'Tamaziɣt Taqbaylit'
    _lang_id = 0x1000


class Kako(Language):
    ISO639_2 = 'kkj'
    english_name = 'Kako'
    native_name = u'Kako'
    _lang_id = 0x1000


class Kalenjin(Language):
    ISO639_2 = 'kln'
    english_name = 'Kalenjin'
    native_name = u'Kalenjin'
    _lang_id = 0x1000


class Kamba(Language):
    ISO639_2 = 'kam'
    english_name = 'Kamba'
    native_name = u'Kamba'
    _lang_id = 0x1000


class Kannada(Language):
    ISO639_1 = 'kn'
    ISO639_2 = 'kan'
    english_name = 'Kannada'
    native_name = u'ಕನ್ನಡ'
    _lang_id = 0x004B


class Kashmiri(Language):
    ISO639_1 = 'ks'
    ISO639_2 = 'kas'
    english_name = 'Kashmiri'
    native_name = u'कॉशुर'
    _lang_id = 0x0060


class KashmiriArab(Language):
    ISO639_1 = 'ks'
    ISO639_2 = 'kas'
    ISO639_3 = 'ks-Arab'
    english_name = 'Kashmiri (Arab)'
    native_name = u'كأشُر'
    _lang_id = 0x0460


class Kazakh(Language):
    ISO639_1 = 'kk'
    ISO639_2 = 'kaz'
    english_name = 'Kazakh'
    native_name = u'қазақ тілі'
    _lang_id = 0x003F


class Khmer(Language):
    ISO639_1 = 'km'
    ISO639_2 = 'khm'
    english_name = 'Khmer'
    native_name = u'ភាសាខ្មែរ'
    _lang_id = 0x0053


class Kiche(Language):
    ISO639_2 = 'quc'
    ISO639_3 = 'quc-Latn'
    english_name = 'K\'iche'
    native_name = u'Qatzijob\'al'
    _lang_id = 0x0086


class Kikuyu(Language):
    ISO639_1 = 'ki'
    ISO639_2 = 'kik'
    english_name = 'Kikuyu'
    native_name = u'Gĩkũyũ'
    _lang_id = 0x1000


class Kinyarwanda(Language):
    ISO639_1 = 'rw'
    ISO639_2 = 'kin'
    english_name = 'Kinyarwanda'
    native_name = u'Kinyarwanda'
    _lang_id = 0x0087


class Konkani(Language):
    ISO639_2 = 'kok'
    english_name = 'Konkani'
    native_name = u'कोंकणी'
    _lang_id = 0x0057


class Kalaallisut(Language):
    ISO639_1 = 'kl'
    ISO639_2 = 'kal'
    english_name = 'Kalaallisut'
    native_name = u'Kalaallisut'
    _lang_id = 0x006F


class KaraKalpak(Language):
    ISO639_2 = 'kaa'
    english_name = 'Karakalpak'
    native_name = u'Қарақалпақ тили'


class Korean(Language):
    ISO639_1 = 'ko'
    ISO639_2 = 'kor'
    english_name = 'Korean'
    native_name = u'한국어'
    _lang_id = 0x0012


class KoyraChiini(Language):
    ISO639_2 = 'khq'
    english_name = 'Koyra Chiini'
    native_name = u'Koyra Chiini'
    _lang_id = 0x1000


class KoyraboroSenni(Language):
    ISO639_2 = 'ses'
    english_name = 'Koyraboro Senni'
    native_name = u'Koyraboro Senni'
    _lang_id = 0x1000


class Kurdish(Language):
    ISO639_1 = 'ku'
    ISO639_2 = 'kur'
    english_name = 'Kurdish'
    native_name = u'کوردی'


class Kwasio(Language):
    ISO639_2 = 'nmg'
    english_name = 'Kwasio'
    native_name = u'Kwasio'
    _lang_id = 0x1000


class Kyrgyz(Language):
    ISO639_1 = 'ky'
    ISO639_2 = 'kir'
    english_name = 'Kyrgyz'
    native_name = u'кыргыз тили'
    _lang_id = 0x0040


class Lakota(Language):
    ISO639_2 = 'lkt'
    english_name = 'Lakota'
    native_name = u'Lakota'
    _lang_id = 0x1000


class Langi(Language):
    ISO639_2 = 'lag'
    english_name = 'Langi'
    native_name = u'Langi'
    _lang_id = 0x1000


class Lao(Language):
    ISO639_1 = 'lo'
    ISO639_2 = 'lao'
    english_name = 'Lao'
    native_name = u'ພາສາລາວ'
    _lang_id = 0x0054


class Latvian(Language):
    ISO639_1 = 'lv'
    ISO639_2 = 'lav'
    english_name = 'Latvian'
    native_name = u'Latviešu valoda'
    _lang_id = 0x0026


class Lingala(Language):
    ISO639_1 = 'ln'
    ISO639_2 = 'lin'
    english_name = 'Lingala'
    native_name = u'Lingala'
    _lang_id = 0x1000


class Lithuanian(Language):
    ISO639_1 = 'lt'
    ISO639_2 = 'lit'
    english_name = 'Lithuanian'
    native_name = u'lietuvių kalba'
    _lang_id = 0x0027


class LowGerman(Language):
    ISO639_2 = 'nds'
    english_name = 'Low German'
    native_name = u'Plattdütsch'
    _lang_id = 0x1000


class LowerSorbian(Language):
    ISO639_2 = 'dsb'
    english_name = 'Lower Sorbian'
    native_name = u'Dolnoserbšćina'
    _lang_id = 0x7C2E


class LubaKatanga(Language):
    ISO639_1 = 'lu'
    ISO639_2 = 'lub'
    english_name = 'Luba-Katanga'
    native_name = u'Kiluba'
    _lang_id = 0x1000


class Luo(Language):
    ISO639_2 = 'luo'
    english_name = 'Luo'
    native_name = u'Dholuo'
    _lang_id = 0x1000


class Luxembourgish(Language):
    ISO639_1 = 'lb'
    ISO639_2 = 'ltz'
    english_name = 'Luxembourgish'
    native_name = u'Lëtzebuergesch'
    _lang_id = 0x006E


class Luyia(Language):
    ISO639_2 = 'luy'
    english_name = 'Luyia'
    native_name = u'Luyia'
    _lang_id = 0x1000


class Macedonian(Language):
    ISO639_1 = 'mk'
    ISO639_2 = 'mac'
    english_name = 'Macedonian'
    native_name = u'македонски јазик'
    _lang_id = 0x002F


class Machame(Language):
    ISO639_2 = 'jmc'
    english_name = 'Machame'
    native_name = u'Machame'
    _lang_id = 0x1000


class MakhuwaMeetto(Language):
    ISO639_2 = 'mgh'
    english_name = 'Makhuwa-Meetto'
    native_name = u'Makhuwa-Meetto'
    _lang_id = 0x1000


class Makonde(Language):
    ISO639_2 = 'kde'
    english_name = 'Makonde'
    native_name = u'Makonde'
    _lang_id = 0x1000


class Malagasy(Language):
    ISO639_1 = 'mg'
    ISO639_2 = 'mlg'
    english_name = 'Malagasy'
    native_name = u'Malagasy'
    _lang_id = 0x1000


class Malay(Language):
    ISO639_1 = 'ms'
    ISO639_2 = 'may'
    english_name = 'Malay'
    native_name = u'Bahasa Melayu'
    _lang_id = 0x003E


class Malayalam(Language):
    ISO639_1 = 'ml'
    ISO639_2 = 'mal'
    english_name = 'Malayalam'
    native_name = u'മലയാളം'
    _lang_id = 0x004C


class Maltese(Language):
    ISO639_1 = 'mt'
    ISO639_2 = 'mlt'
    english_name = 'Maltese'
    native_name = u'Malti'
    _lang_id = 0x003A


class Manx(Language):
    ISO639_1 = 'gv'
    english_name = 'Manx'
    native_name = u'Gaelg'
    _lang_id = 0x1000


class Maori(Language):
    ISO639_1 = 'mi'
    ISO639_2 = 'mao'
    english_name = 'Maori'
    native_name = u'Te Reo Māori'
    _lang_id = 0x0081


class Marathi(Language):
    ISO639_1 = 'mr'
    ISO639_2 = 'mar'
    english_name = 'Marathi'
    native_name = u'मराठी'
    _lang_id = 0x004E


class Mapudungun(Language):
    ISO639_2 = 'arn'
    english_name = 'Mapudungun'
    native_name = u'Mapudungun'
    _lang_id = 0x007A


class Masai(Language):
    ISO639_2 = 'mas'
    english_name = 'Masai'
    native_name = u'ɔl'
    _lang_id = 0x1000


class Mazanderani(Language):
    ISO639_2 = 'mzn'
    english_name = 'Mazanderani'
    native_name = u'Mazanderani'
    _lang_id = 0x1000


class Meru(Language):
    ISO639_1 = 'ml'
    ISO639_2 = 'mer'
    english_name = 'Meru'
    native_name = u'Meru'
    _lang_id = 0x1000


class Meta(Language):
    ISO639_2 = 'mgo'
    english_name = 'Meta\''
    native_name = u'Meta\''
    _lang_id = 0x1000


class Mohawk(Language):
    ISO639_2 = 'moh'
    english_name = 'Mohawk'
    native_name = u'Kanien’kéha'
    _lang_id = 0x007C


class Mongolian(Language):
    ISO639_1 = 'mn'
    ISO639_2 = 'mon'
    english_name = 'Mongolian'
    native_name = u'ᠮᠣᠩᠭᠣᠯ ᠬᠡᠯᠡ'
    _lang_id = 0x0050


class MongolianCyrillic(Language):
    ISO639_1 = 'mn'
    ISO639_2 = 'mon'
    ISO639_3 = 'mn-Cryl'
    english_name = 'Mongolian (Cyrillic)'
    native_name = u'монгол хэл'
    _lang_id = 0x7850


class MongolianTraditional(Language):
    ISO639_1 = 'mn'
    ISO639_2 = 'mon'
    ISO639_3 = 'mn-Mong'
    english_name = 'Mongolian (Traditional)'
    native_name = u'ᠮᠣᠩᠭᠣᠯ ᠬᠡᠯᠡ'
    _lang_id = 0x7C50


class Morisyen(Language):
    ISO639_2 = 'mfe'
    english_name = 'Morisyen'
    native_name = u'Kreol morisien'
    _lang_id = 0x1000


class Marshallese(Language):
    ISO639_1 = 'mh'
    ISO639_2 = 'mah'
    english_name = 'Marshallese'
    native_name = u'Kajin M̧ajeļ'


class Mundang(Language):
    ISO639_2 = 'mua'
    english_name = 'Mundang'
    native_name = u'Mundang'
    _lang_id = 0x1000


class Nauru(Language):
    ISO639_1 = 'na'
    ISO639_2 = 'nau'
    english_name = 'Nauru'
    native_name = u'dorerin Naoero'


class Nko(Language):
    ISO639_2 = 'nqo'
    english_name = 'N\'ko'
    native_name = u'N\'ko'
    _lang_id = 0x1000


class Nama(Language):
    ISO639_2 = 'naq'
    english_name = 'Nama'
    native_name = u'Nama'
    _lang_id = 0x1000


class Nepali(Language):
    ISO639_1 = 'ne'
    ISO639_2 = 'nep'
    english_name = 'Nepali'
    native_name = u'नेपाली भाषा'
    _lang_id = 0x0061


class Ngiemboon(Language):
    ISO639_2 = 'nnh'
    english_name = 'Ngiemboon'
    native_name = u'Ngiemboon'
    _lang_id = 0x1000


class Ngomba(Language):
    ISO639_2 = 'jgo'
    english_name = 'Ngomba'
    native_name = u'Ngomba'
    _lang_id = 0x1000


class NorthernLuri(Language):
    ISO639_2 = 'irc'
    english_name = 'Northern Luri'
    native_name = u'Northern Luri'
    _lang_id = 0x1000


class NorthNdebele(Language):
    ISO639_1 = 'nd'
    ISO639_2 = 'nde'
    english_name = 'North Ndebele'
    native_name = u'saseNyakatho'
    _lang_id = 0x1000


class NorthFrisian(Language):
    ISO639_2 = 'frr'
    english_name = 'North Frisian'
    native_name = u'Frasch'


class Norwegian(Language):
    ISO639_1 = 'no'
    ISO639_2 = 'nor'
    english_name = 'Norwegian'
    native_name = u'norsk'
    _lang_id = 0x0014


class NorwegianNynorsk(Language):
    ISO639_1 = 'nn'
    ISO639_2 = 'nno'
    english_name = 'Norwegian (Nynorsk)'
    native_name = u'nynorsk'
    _lang_iid = 0x7814


class NorwegianBokmal(Language):
    ISO639_1 = 'nb'
    ISO639_2 = 'nob'
    english_name = 'Norwegian (Bokmal)'
    native_name = u'bokmål'
    _lang_id = 0x7C14


class Niuean(Language):
    ISO639_2 = 'niu'
    english_name = 'Niuean'
    native_name = u'ko e vagahau Niuē'


class Nuer(Language):
    ISO639_2 = 'nus'
    english_name = 'Nuer'
    native_name = u'Nuer'
    _lang_id = 0x1000


class Nyanja(Language):
    ISO639_1 = 'ny'
    ISO639_2 = 'nya'
    english_name = 'Nyanja'
    native_name = u'chiCheŵa'


class Nyankole(Language):
    ISO639_2 = 'nyn'
    english_name = 'Nyankole'
    native_name = u'Nyankole'
    _lang_id = 0x1000


class Occitan(Language):
    ISO639_1 = 'oc'
    ISO639_2 = 'oci'
    english_name = 'Occitan'
    native_name = u'lenga d\'òc'
    _lang_id = 0x0082


class Oriya(Language):
    ISO639_1 = 'or'
    ISO639_2 = 'ori'
    english_name = 'Oriya'
    native_name = u'ଓଡ଼ିଆ'
    _lang_id = 0x0048


class Oromo(Language):
    ISO639_1 = 'om'
    ISO639_2 = 'orm'
    english_name = 'Oromo'
    native_name = u'Afaan Oromoo'
    _lang_id = 0x0072


class Ossetian(Language):
    ISO639_1 = 'os'
    ISO639_2 = 'oss'
    english_name = 'Ossetian'
    native_name = u'Ирон æвзаг'
    _lang_id = 0x1000


class Papiamento(Language):
    ISO639_2 = 'pap'
    english_name = 'Papiamento'
    native_name = u'Papiamentu'


class Palauan(Language):
    ISO639_2 = 'pau'
    english_name = 'Palauan'
    native_name = u'a tekoi er a Belau'


class Pashto(Language):
    ISO639_1 = 'ps'
    ISO639_2 = 'pus'
    english_name = 'Pashto'
    native_name = u'پښتو'
    _lang_id = 0x0063


class Persian(Language):
    ISO639_1 = 'fa'
    ISO639_2 = 'fas'
    english_name = 'Persian'
    native_name = u'فارسی'
    _lang_id = 0x0029


class PitcairnNorfolk(Language):
    ISO639_2 = 'pih'
    english_name = 'Pitcairn-Norfolk'
    native_name = u'Norfuk'


class Polish(Language):
    ISO639_1 = 'pl'
    ISO639_2 = 'pol'
    english_name = 'Polish'
    native_name = u'Język polski'
    _lang_id = 0x0015


class Portuguese(Language):
    ISO639_1 = 'pt'
    ISO639_2 = 'por'
    english_name = 'Portuguese'
    native_name = u'português'
    _lang_id = 0x0016


class Prussian(Language):
    ISO639_3 = 'prg-001'
    english_name = 'Prussian'
    native_name = u'Prussian'
    _lang_id = 0x1000


class Punjabi(Language):
    ISO639_1 = 'pa'
    ISO639_2 = 'pan'
    english_name = 'Punjabi'
    native_name = u'ਪੰਜਾਬੀ'
    _lang_id = 0x0046


class PunjabiArabic(Language):
    ISO639_1 = 'pa'
    ISO639_2 = 'pan'
    english_name = 'Punjabi (Arabic)'
    native_name = u'پنجابی'
    _lang_id = 0x7C46


class Quechua(Language):
    ISO639_1 = 'qu'
    ISO639_2 = 'que'
    english_name = 'Quechua'
    native_name = u'Runa simi'
    lang_id = 0x006B


class Ripuarian(Language):
    ISO639_2 = 'ksh'
    english_name = 'Ripuarian'
    native_name = u'Ripuarian'
    lang_id = 0x1000


class Rarotongan(Language):
    ISO639_2 = 'rar'
    english_name = 'Rarotongan'
    native_name = u'Māori Kūki \'Āirani'


class Romani(Language):
    ISO639_2 = 'rom'
    english_name = 'Romani'
    native_name = u'romani čhib'


class Romanian(Language):
    ISO639_1 = 'ro'
    ISO639_2 = 'rum'
    english_name = 'Romanian'
    native_name = u'limba română'
    _lang_id = 0x0018


class Romansh(Language):
    ISO639_1 = 'rm'
    ISO639_2 = 'roh'
    english_name = 'Romansh'
    native_name = u'Rumàntsch'
    _lang_id = 0x0017


class Rombo(Language):
    ISO639_2 = 'rof'
    english_name = 'Rombo'
    native_name = u'Rombo'
    _lang_id = 0x1000


class Rundi(Language):
    ISO639_1 = 'rn'
    ISO639_2 = 'run'
    english_name = 'Rundi'
    native_name = u'Ikirundi'
    _lang_id = 0x1000


class Russian(Language):
    ISO639_1 = 'ru'
    ISO639_2 = 'rus'
    english_name = 'Russian'
    native_name = u'русский язык'
    _lang_id = 0x0019


class Rwa(Language):
    ISO639_2 = 'rwk'
    english_name = 'Rwa'
    native_name = u'Rwa'
    _lang_id = 0x1000


class Saho(Language):
    ISO639_2 = 'ssy'
    english_name = 'Saho'
    native_name = u'Saho'
    _lang_id = 0x1000


class Yakut(Language):
    ISO639_2 = 'sah'
    english_name = 'Yakut'
    native_name = u'Сахалыы'
    _lang_id = 0x0085


class Samburu(Language):
    ISO639_2 = 'saq'
    english_name = 'Samburu'
    native_name = u'Samburu'
    _lang_id = 0x1000


class SamiInari(Language):
    ISO639_2 = 'smn'
    english_name = 'Inari Sami'
    native_name = u'anarâškielâ'
    _lang_id = 0x703B


class SamiLule(Language):
    ISO639_2 = 'smj'
    english_name = 'Lule Sami'
    native_name = u'julevsámegiella'
    _lang_id = 0x7C3B


class SamiNorthern(Language):
    ISO639_1 = 'se'
    ISO639_2 = 'sme'
    english_name = 'Northern Sami'
    native_name = u'davvisámegiella'
    _lang_id = 0x003B


class SamiSkolt(Language):
    ISO639_2 = 'sms'
    english_name = 'Skolt Sami'
    native_name = u'sääʹmǩiõll'
    _lang_id = 0x743B


class SamiSouthern(Language):
    ISO639_2 = 'sma'
    english_name = 'Southern Sami'
    native_name = u'Åarjelsaemien gïele'
    _lang_id = 0x783B


class Samoan(Language):
    ISO639_1 = 'sm'
    ISO639_2 = 'smo'
    english_name = 'Samoan'
    native_name = u'Gagana faʻa Sāmoa'


class Sango(Language):
    ISO639_1 = 'sg'
    ISO639_2 = 'sag'
    english_name = 'Sango'
    native_name = u'yângâ tî sängö'
    _lang_id = 0x1000


class Sangu(Language):
    ISO639_2 = 'sbp'
    english_name = 'Sangu'
    native_name = u'Sangu'
    _lang_id = 0x1000


class Sanskrit(Language):
    ISO639_1 = 'sa'
    ISO639_2 = 'san'
    english_name = 'Sanskrit'
    native_name = u'संस्कृतम्'
    _lang_id = 0x004F


class SaterlandFrisian(Language):
    ISO639_2 = 'frs'
    english_name = 'Saterland Frisian'
    native_name = u'Seeltersk'


class ScottishGaelic(Language):
    ISO639_1 = 'gd'
    ISO639_2 = 'gla'
    english_name = 'Scottish Gaelic'
    native_name = u'Gàidhlig'
    _lang_id = 0x0091


class Sena(Language):
    ISO639_2 = 'seh'
    english_name = 'Sena'
    native_name = u'Sena'
    _lang_id = 0x1000


class Serbian(Language):
    ISO639_1 = 'sr'
    ISO639_2 = 'srp'
    english_name = 'Serbian'
    native_name = u'Serbian'
    _lang_id = 0x7C1A


class SerbianCyrillic(Language):
    ISO639_1 = 'sr'
    ISO639_2 = 'srp'
    ISO639_3 = 'sr-Cryl'
    english_name = 'Serbian (Cyrillic)'
    native_name = u'српски'
    _lang_id = 0x6C1A


class SerbianLatin(Language):
    ISO639_1 = 'sr'
    ISO639_2 = 'srp'
    ISO639_3 = 'sr-Latn'
    english_name = 'Serbian (Latin)'
    native_name = u'srpski'
    _lang_id = 0x701A


class Tswana(Language):
    ISO639_1 = 'tn'
    ISO639_2 = 'tsn'
    english_name = 'Tswana'
    native_name = u'Setswana'
    _lang_id = 0x0032


class SeychelloisCreole(Language):
    ISO639_2 = 'crs'
    english_name = 'Seychellois Creole'
    native_name = u'créole seychellois'


class Shambala(Language):
    ISO639_2 = 'ksb'
    english_name = 'Shambala'
    native_name = u'Shambala'
    _lang_id = 0x1000


class Shona(Language):
    ISO639_1 = 'sn'
    ISO639_2 = 'sna'
    english_name = 'Shona'
    native_name = u'chiShona'
    _lang_id = 0x1000


class Sindhi(Language):
    ISO639_1 = 'sd'
    english_name = 'Sindhi'
    native_name = u'सिन्धी'
    _lang_id = 0x0059


class SindhiArab(Language):
    ISO639_3 = 'sd-Arab'
    english_name = 'Sindhi (Arab)'
    native_name = u'سنڌي'
    _lang_id = 0x7C59


class Sinhala(Language):
    ISO639_1 = 'si'
    ISO639_2 = 'sin'
    english_name = 'Sinhala'
    native_name = u'සිංහල'
    _lang_id = 0x005B


class Slovak(Language):
    ISO639_1 = 'sk'
    ISO639_2 = 'slo'
    english_name = 'Slovak'
    native_name = u'slovenský jazyk'
    _lang_id = 0x001B


class Slovenian(Language):
    ISO639_1 = 'sl'
    ISO639_2 = 'slv'
    english_name = 'Slovenian'
    native_name = u'slovenščina'
    _lang_id = 0x0024


class Soga(Language):
    ISO639_2 = 'xog'
    english_name = 'Soga'
    native_name = u'Soga'
    _lang_id = 0x1000


class Somali(Language):
    ISO639_1 = 'so'
    ISO639_2 = 'som'
    english_name = 'Somali'
    native_name = u'af Soomaali'
    _lang_id = 0x0077


class Sotho(Language):
    ISO639_1 = 'st'
    ISO639_2 = 'sot'
    english_name = 'Sotho'
    native_name = u'Sesotho'
    _lang_id = 0x0030


class SothoNorthern(Language):
    ISO639_2 = 'nso'
    english_name = 'Northern Sotho'
    native_name = u'Sesotho sa Leboa'
    _lang_id = 0x006C


class SothoSouthern(Language):
    ISO639_1 = 'st'
    ISO639_2 = 'sot'
    english_name = 'Southern Sotho'
    native_name = u'Sesotho [southern]'
    _lang_id = 0x1000


class SouthNdebele(Language):
    ISO639_1 = 'nr'
    english_name = 'South Ndebele'
    native_name = u'isiNdebele seSewula'
    _lang_id = 0x1000


class Spanish(Language):
    ISO639_1 = 'es'
    ISO639_2 = 'spa'
    english_name = 'Spanish'
    native_name = u'Español'
    _lang_id = 0x000A


class StandardMoroccanTamazight(Language):
    ISO639_2 = 'zgh'
    english_name = 'Standard Moroccan Tamazight'
    native_name = u'ⵜⴰⵎⴰⵣⵉⵖⵜ ⵜⴰⵏⴰⵡⴰⵢⵜ'
    _lang_id = 0x1000


class Swati(Language):
    ISO639_1 = 'ss'
    ISO639_2 = 'ssw'
    english_name = 'Swati'
    native_name = u'siSwati'
    _lang_id = 0x1000


class Swedish(Language):
    ISO639_1 = 'sv'
    ISO639_2 = 'swe'
    english_name = 'Swedish'
    native_name = u'svenska'
    _lang_id = 0x001D


class Syriac(Language):
    ISO639_2 = 'syr'
    english_name = 'Syriac'
    native_name = u'ܠܫܢܐ ܣܘܪܝܝܐ'
    _lang_id = 0x005A


class Swahili(Language):
    ISO639_1 = 'sw'
    ISO639_2 = 'swa'
    english_name = 'Swahili'
    native_name = u'Kiswahili'
    _lang_id = 0x0041


class Tachelhit(Language):
    ISO639_2 = 'shi'
    english_name = 'Tachelhit'
    native_name = u'Tachelhit'
    _lang_id = 0x1000


class TachelhitLatin(Language):
    ISO639_3 = 'shi-Latn'
    english_name = 'Tachelhit (Latin)'
    native_name = u'Tachelhit (Latin)'
    _lang_id = 0x1000


class Tagalog(Language):
    ISO639_1 = 'tl'
    ISO639_2 = 'tgl'
    english_name = 'Tagalog'
    native_name = u'Wikang Tagalog'


class Taita(Language):
    ISO639_2 = 'dav'
    english_name = 'Taita'
    native_name = u'Taita'
    _lang_id = 0x1000


class Tajik(Language):
    ISO639_1 = 'tg'
    ISO639_2 = 'tgk'
    english_name = 'Tajik'
    native_name = u'tojikī'
    _lang_id = 0x0028


class TajikCyrillic(Language):
    ISO639_3 = 'tg-Cyrl'
    english_name = 'Tajik (Cyrillic)'
    native_name = u'тоҷикӣ'
    _lang_id = 0x7C28


class Tamazight(Language):
    ISO639_2 = 'tzm'
    english_name = 'Tamazight'
    native_name = u'Tamazight'
    _lang_id = 0x005F


class TamazightLatin(Language):
    ISO639_3 = 'tzm-Latn'
    english_name = 'Tamazight (Latin)'
    native_name = u'Tamazight'
    _lang_id = 0x7C5F


class Tamil(Language):
    ISO639_1 = 'ta'
    ISO639_2 = 'tam'
    english_name = 'Tamil'
    native_name = u'தமிழ்'
    _lang_id = 0x0049


class Tasawaq(Language):
    ISO639_2 = 'twq'
    english_name = 'Tasawaq'
    native_name = u'Tasawaq'
    _lang_id = 0x1000


class Tatar(Language):
    ISO639_1 = 'tt'
    ISO639_2 = 'tat'
    english_name = 'Tatar'
    native_name = u'татар теле'
    _lang_id = 0x0044


class Telugu(Language):
    ISO639_1 = 'te'
    ISO639_2 = 'tel'
    english_name = 'Telugu'
    native_name = u'తెలుగు'
    _lang_id = 0x004A


class Teso(Language):
    ISO639_2 = 'teo'
    english_name = 'Teso'
    native_name = u'Teso'
    _lang_id = 0x1000


class Tetum(Language):
    ISO639_2 = 'tet'
    english_name = 'Tetum'
    native_name = u'Lia-Tetun'


class Thai(Language):
    ISO639_1 = 'th'
    ISO639_2 = 'tha'
    english_name = 'Thai'
    native_name = u'ภาษาไทย'
    _lang_id = 0x001E


class Tibetan(Language):
    ISO639_1 = 'bo'
    english_name = 'Tibetan'
    native_name = u'ལྷ་སའི་སྐད་'
    _lang_id = 0x0051


class Tigre(Language):
    ISO639_2 = 'tig'
    english_name = 'Tigre'
    native_name = u'ትግራይት'
    _lang_id = 0x1000


class Tigrinya(Language):
    ISO639_1 = 'ti'
    ISO639_2 = 'tir'
    english_name = 'Tigrinya'
    native_name = u'ትግርኛ'
    _lang_id = 0x0073


class Tobian(Language):
    ISO639_3 = 'tox'
    english_name = 'Tobian'
    native_name = u'ramarih Hatohobei'


class Tokelauan(Language):
    ISO639_2 = 'tkl'
    english_name = 'Tokelauan'
    native_name = u'Fakatokelau'


class TokPisin(Language):
    ISO639_2 = 'tpi'
    english_name = 'Tok Pisin'
    native_name = u'Tok Pisin'


class Tongan(Language):
    ISO639_1 = 'to'
    english_name = 'Tongan'
    native_name = u'lea faka-Tonga'
    _lang_id = 0x1000


class Tsonga(Language):
    ISO639_1 = 'ts'
    ISO639_2 = 'tso'
    english_name = 'Tsonga'
    native_name = u'Xitsonga'
    _lang_id = 0x0031


class Turkish(Language):
    ISO639_1 = 'tr'
    ISO639_2 = 'tur'
    english_name = 'Turkish'
    native_name = u'Türkçe'
    _lang_id = 0x001F


class Turkmen(Language):
    ISO639_1 = 'tk'
    ISO639_2 = 'tuk'
    english_name = 'Turkmen'
    native_name = u'Türkmençe'
    _lang_id = 0x0042


class Ukrainian(Language):
    ISO639_1 = 'uk'
    ISO639_2 = 'ukr'
    english_name = 'Ukrainian'
    native_name = u'українська мова'
    _lang_id = 0x0022


class UpperSorbian(Language):
    ISO639_2 = 'hsb'
    english_name = 'Upper Sorbian'
    native_name = u'hornjoserbšćina'
    _lang_id = 0x002E


class Urdu(Language):
    ISO639_1 = 'ur'
    ISO639_2 = 'urd'
    english_name = 'Urdu'
    native_name = u'اُردُو'
    _lang_id = 0x0020


class Uyghur(Language):
    ISO639_1 = 'ug'
    ISO639_2 = 'uig'
    english_name = 'Uyghur'
    native_name = u'ئۇيغۇرچە'
    _lang_id = 0x0080


class UzbekArab(Language):
    ISO639_1 = 'uz'
    ISO639_2 = 'uzb'
    ISO639_3 = 'uzb-Arab'
    english_name = 'Uzbek (Arab)'
    native_name = u'ئوبېک تیلی'
    _lang_id = 0x1000


class UzbekCyrillic(Language):
    ISO639_1 = 'uz'
    ISO639_2 = 'uzb'
    ISO639_3 = 'uzb-Cyrl'
    english_name = 'Uzbek (Cyrillic)'
    native_name = u'ўзбекча'
    _lang_id = 0x7843


class UzbekLatin(Language):
    ISO639_1 = 'uz'
    ISO639_2 = 'uzb'
    ISO639_3 = 'uzb-Latn'
    english_name = 'Uzbek (Latin)'
    native_name = u'O\'zbekcha'
    _lang_id = 0x0043


class Vai(Language):
    ISO639_2 = 'vai'
    english_name = 'Vai'
    native_name = u'ꕙꔤ'
    _lang_id = 0x1000


class VaiLatin(Language):
    ISO639_3 = 'vai-Latn'
    english_name = 'Vai (Latin)'
    native_name = u'Vai (Latin)'
    _lang_id = 0x1000


class Valencian(Language):
    ISO639_1 = 'ca'
    english_name = 'Valencian'
    native_name = u'Valencian'
    _lang_id = 0x0803


class Venda(Language):
    ISO639_1 = 've'
    ISO639_2 = 'ven'
    english_name = 'Venda'
    native_name = u'Tshivenḓa'
    _lang_id = 0x0033


class Vietnamese(Language):
    ISO639_1 = 'vi'
    ISO639_2 = 'vie'
    english_name = 'Vietnamese'
    native_name = u'Tiếng Việt'
    _lang_id = 0x002A


class Volapuk(Language):
    ISO639_1 = 'vo'
    ISO639_2 = 'vol'
    english_name = 'Volapuk'
    native_name = u'Volapük'
    _lang_id = 0x1000


class Vunjo(Language):
    ISO639_2 = 'vun'
    english_name = 'Vunjo'
    native_name = u'Vunjo'
    _lang_id = 0x1000


class Walser(Language):
    ISO639_2 = 'wae'
    english_name = 'Walser'
    native_name = u'Walser'
    _lang_id = 0x1000


class Welsh(Language):
    ISO639_1 = 'cy'
    ISO639_2 = 'wel'
    english_name = 'Welsh'
    native_name = u'y Gymraeg'
    _lang_id = 0x0052


class Walamo(Language):
    ISO639_2 = 'wal'
    english_name = 'Walamo'
    native_name = u'Walamo'
    _lang_id = 0x1000


class Wolof(Language):
    ISO639_1 = 'wo'
    ISO639_2 = 'wol'
    english_name = 'Wolof'
    native_name = u'Wolof'
    _lang_id = 0x0088


class Xhosa(Language):
    ISO639_1 = 'xh'
    ISO639_2 = 'xho'
    english_name = 'Xhosa'
    native_name = u'isiXhosa'
    _lang_id = 0x0034


class Yangben(Language):
    ISO639_2 = 'yav'
    english_name = 'Yangben'
    native_name = u'Yangben'
    _lang_id = 0x1000


class SichuanYi(Language):
    ISO639_1 = 'ii'
    ISO639_2 = 'iii'
    english_name = 'Sichuan Yi'
    native_name = u'ꆈꌠꉙ'
    _lang_id = 0x0078


class Yoruba(Language):
    ISO639_1 = 'yo'
    ISO639_2 = 'yor'
    english_name = 'Yoruba'
    native_name = u'èdè Yorùbá'
    _lang_id = 0x006A


class Zarma(Language):
    ISO639_2 = 'dje'
    english_name = 'Zarma'
    native_name = u'Zarma'
    _lang_id = 0x1000


class Zulu(Language):
    ISO639_1 = 'zu'
    ISO639_2 = 'zul'
    english_name = 'Zulu'
    native_name = u'isiZulu'
    _lang_id = 0x0035


class Afghanistan(Locale):
    _iso_code = 'AF'
    english_name = 'Afghanistan'
    _flag = 'flags\\AF.png'
    languages = [
        Persian(u'د افغانستان اسلامي دولتدولت اسلامی افغانستان', lcid=0x1000),
        Pashto(u'جمهوری اسلامی افغانستان', lcid=0x0463),
        Dari(u'افغانستان', lcid=0x048C),
        UzbekArab(u'', lcid=0x1000)
    ]


class AlandIslands(Locale):
    _iso_code = 'AX'
    english_name = 'Aland Islands'
    _flag = 'flags\\AX.png'
    languages = [
        Swedish(u'Åland', lcid=0x1000)
    ]


class Albania(Locale):
    _iso_code = 'AL'
    english_name = 'Albania'
    _flag = 'flags\\AL.png'
    languages = [
        Albanian(u'Shqipëria', lcid=0x041C)
    ]


class Algeria(Locale):
    _iso_code = 'DZ'
    english_name = 'Algeria'
    _flag = 'flags\\DZ.png'
    languages = [
        Arabic(u'الجزائر', lcid=0x1401),
        French(u'', lcid=0x000C),
        Kabyle(u'', lcid=0x1000),
        TamazightLatin(u'', lcid=0x1000)
    ]


class AmericanSamoa(Locale):
    _iso_code = 'AS'
    english_name = 'American Samoa'
    _flag = 'flags\\AS.png'
    languages = [
        English(u'American Samoa', lcid=0x1000),
        Samoan(u'Amerika Sāmoa', lcid=None)
    ]


class Andorra(Locale):
    _iso_code = 'AD'
    english_name = 'Andorra'
    _flag = 'flags\\AD.png'
    languages = [
        Catalan(u'Andorra', lcid=0x1000)
    ]


class Angola(Locale):
    _iso_code = 'AO'
    english_name = 'Angola'
    _flag = 'flags\\AO.png'
    languages = [
        Portuguese(u'Angola', lcid=0x1000),
        Lingala(u'Ngola', lcid=0x1000)
    ]


class Anguilla(Locale):
    _iso_code = 'AI'
    english_name = 'Anguilla'
    _flag = 'flags\\AI.png'
    languages = [
        English(u'Anguilla', lcid=0x1000)
    ]


class Antarctica(Locale):
    _iso_code = 'AQ'
    english_name = 'Antarctica'
    _flag = 'flags\\AQ.png'
    languages = [
        English(u'Antarctica', lcid=0x1000),
        Spanish(u'Antártico', lcid=None),
        French(u'Antarctique', lcid=None),
        Russian(u'Антарктике', lcid=None)
    ]


class AntiguaBarbuda(Locale):
    _iso_code = 'AG'
    english_name = 'Antigua and Barbuda'
    _flag = 'flags\\AG.png'
    languages = [
        English(u'Antigua and Barbuda', lcid=0x1000)
    ]


class Argentina(Locale):
    _iso_code = 'AR'
    english_name = 'Argentina'
    _flag = 'flags\\AR.png'
    languages = [
        Spanish(u'Argentina', lcid=0x2C0A)
    ]


class Armenia(Locale):
    _iso_code = 'AM'
    english_name = 'Armenia'
    _flag = 'flags\\AM.png'
    languages = [
        Armenian(u'Հայաստան', lcid=0x042B)
    ]


class Aruba(Locale):
    _iso_code = 'AW'
    english_name = 'Aruba'
    _flag = 'flags\\AW.png'
    languages = [
        Dutch(u'Aruba', lcid=0x1000),
        Papiamento(u'Aruba', lcid=None)
    ]


class Australia(Locale):
    _iso_code = 'AU'
    english_name = 'Australia'
    _flag = 'flags\\AU.png'
    languages = [
        English(u'Australia', lcid=0x0C09)
    ]


class Austria(Locale):
    _iso_code = 'AT'
    english_name = 'Austria'
    _flag = 'flags\\AT.png'
    languages = [
        German(u'Österreich', lcid=0x0C07),
        English(u'Austria', lcid=0x0009)
    ]


class Azerbaijan(Locale):
    _iso_code = 'AZ'
    english_name = 'Azerbaijan'
    _flag = 'flags\\AZ.png'
    languages = [
        Azerbaijani(u'Azərbaycan', lcid=None),
        AzerbaijaniCyrillic(u'', lcid=0x082C),
        AzerbaijaniLatin(u'', lcid=0x042C)
    ]


class Bahamas(Locale):
    _iso_code = 'BS'
    english_name = 'Bahamas'
    _flag = 'flags\\BS.png'
    languages = [
        English(u'The Bahamas', lcid=0x1000)
    ]


class Bahrein(Locale):
    _iso_code = 'BH'
    english_name = 'Bahrein'
    _flag = 'flags\\BH.png'
    languages = [
        Arabic(u'البحرين', lcid=0x3C01)
    ]


class Bangladesh(Locale):
    _iso_code = 'BD'
    english_name = 'Bangladesh'
    _flag = 'flags\\BD.png'
    languages = [
        Bengali(u'বাংলাদেশ', lcid=0x0845)
    ]


class Barbados(Locale):
    _iso_code = 'BB'
    english_name = 'Barbados'
    _flag = 'flags\\BB.png'
    languages = [
        English(u'Barbados', lcid=0x1000)
    ]


class Belarus(Locale):
    _iso_code = 'BY'
    english_name = 'Belarus'
    _flag = 'flags\\BY.png'
    languages = [
        Belarusian(u'Bielaruś', lcid=0x0423),
        Russian(u'Belarus', lcid=0x1000)
    ]


class Belgium(Locale):
    _iso_code = 'BE'
    english_name = 'Belgium'
    _flag = 'flags\\BE.png'
    languages = [
        German(u'Belgien', lcid=0x1000),
        French(u'Belgique', lcid=0x080C),
        Dutch(u'België', lcid=0x0813),
        English(u'Belgium', lcid=0x0009)
    ]


class Belize(Locale):
    _iso_code = 'BZ'
    english_name = 'Belize'
    _flag = 'flags\\BZ.png'
    languages = [
        English(u'Belize', lcid=0x2809),
        Spanish(u'', lcid=0x000A)
    ]


class Benin(Locale):
    _iso_code = 'BJ'
    english_name = 'Benin'
    _flag = 'flags\\BJ.png'
    languages = [
        French(u'Bénin', lcid=0x1000),
        Yoruba(u'', lcid=0x006A)
    ]


class Bermuda(Locale):
    _iso_code = 'BM'
    english_name = 'Bermuda'
    _flag = 'flags\\BM.png'
    languages = [
        English(u'Bermuda', lcid=0x1000)
    ]


class Bhutan(Locale):
    _iso_code = 'BT'
    english_name = 'Bhutan'
    _flag = 'flags\\BT.png'
    languages = [
        Dzongkha(u'Druk Yul', lcid=None)
    ]


class Bolivia(Locale):
    _iso_code = 'BO'
    english_name = 'Bolivia'
    _flag = 'flags\\BO.png'
    languages = [
        Aymara(u'Wuliwya', lcid=None),
        Spanish(u'Bolivia', lcid=0x400A),
        Guarani(u'Volívia', lcid=None),
        Quechua(u'Buliwya', lcid=None)
    ]


class BosniaHerzegovina(Locale):
    _iso_code = 'BA'
    english_name = 'Bosnia and Herzegovina'
    _flag = 'flags\\BA.png'
    languages = [
        BosnianCyrillic(u'Босна и Херцеговина', lcid=0x201A),
        CroatianLatin(u'Bosna i Hercegovina', lcid=0x101A),
        SerbianCyrillic(u'Босна и Херцеговина', lcid=None),
        BosnianLatin(u'Bosna i Hercegovina', lcid=0x141A),
        SerbianLatin(u'Bosna i Hercegovina', lcid=0x181A)
    ]


class Botswana(Locale):
    _iso_code = 'BW'
    english_name = 'Botswana'
    _flag = 'flags\\BW.png'
    languages = [
        English(u'Botswana', lcid=0x1000),
        Tswana(u'Botswana', lcid=None)
    ]


class BouvetIsland(Locale):
    _iso_code = 'BV'
    english_name = 'Bouvet Island'
    _flag = 'flags\\BV.png'
    languages = [
        Norwegian(u'Bouvetøya', lcid=None)
    ]


class Brazil(Locale):
    _iso_code = 'BR'
    english_name = 'Brazil'
    _flag = 'flags\\BR.png'
    languages = [
        Portuguese(u'Brasil', lcid=0x0416),
        Spanish(u'Brasil', lcid=0x000A)
    ]


class BritishIndianOceanTerritory(Locale):
    _iso_code = 'IO'
    english_name = 'British Indian Ocean Territory'
    _flag = 'flags\\IO.png'
    languages = [
        English(u'British Indian Ocean Territory', lcid=0x1000)
    ]


class BritishVirginIslands(Locale):
    _iso_code = 'VG'
    english_name = 'British Virgin Islands'
    _flag = 'flags\\VG.png'
    languages = [
        English(u'British Virgin Islands', lcid=0x1000)
    ]


class BruneiDarussalam(Locale):
    _iso_code = 'BN'
    english_name = 'Brunei Darussalam'
    _flag = 'flags\\BN.png'
    languages = [
        Malay(u'Brunei', lcid=0x083E)
    ]


class Bulgaria(Locale):
    _iso_code = 'BG'
    english_name = 'Bulgaria'
    _flag = 'flags\\BG.png'
    languages = [
        Bulgarian(u'Bulgariya', lcid=0x0402)
    ]


class BurkinaFaso(Locale):
    _iso_code = 'BF'
    english_name = 'Burkina Faso'
    _flag = 'flags\\BF.png'
    languages = [
        French(u'Burkina Faso', lcid=None)
    ]


class Burundi(Locale):
    _iso_code = 'BI'
    english_name = 'Burundi'
    _flag = 'flags\\BI.png'
    languages = [
        French(u'Burundi', lcid=None),
        English(u'Burundi', lcid=0x0009),
        Rundi(u'Uburundi', lcid=0x1000)
    ]


class CaboVerde(Locale):
    _iso_code = 'CV'
    english_name = 'Cabo Verde'
    _flag = 'flags\\CV.png'
    languages = [
        Portuguese(u'Cabo Verde', lcid=None),
        Kabuverdianu(u'', lcid=0x1000)
    ]


class Cambodia(Locale):
    _iso_code = 'KH'
    english_name = 'Cambodia'
    _flag = 'flags\\KH.png'
    languages = [
        Khmer(u'កម្ពុជា', lcid=0x0453)
    ]


class Cameroon(Locale):
    _iso_code = 'CM'
    english_name = 'Cameroon'
    _flag = 'flags\\CM.png'
    languages = [
        English(u'Cameroon', lcid=0x1000),
        French(u'Cameroun', lcid=None),
        Aghem(u'', lcid=0x1000),
        Bafia(u'', lcid=0x1000),
        Basaa(u'', lcid=0x1000),
        Duala(u'', lcid=0x1000),
        Ewondo(u'', lcid=0x1000),
        Fulah(u'', lcid=0x0067),
        Kako(u'', lcid=0x1000),
        Kwasio(u'', lcid=0x1000),
        Meta(u'', lcid=0x1000),
        Mundang(u'', lcid=0x1000),
        Ngiemboon(u'', lcid=0x1000),
        Ngomba(u'', lcid=0x1000),
        Yangben(u'', lcid=0x1000)
    ]


class Canada(Locale):
    _iso_code = 'CA'
    english_name = 'Canada'
    _flag = 'flags\\CA.png'
    languages = [
        English(u'Canada', lcid=0x1009),
        French(u'Canada', lcid=0x0C0C),
        InuktitutLatin(u'', lcid=0x085D),
        InuktitutSyllabics(u'', lcid=0x045D),
        Mohawk(u'', lcid=0x007C)
    ]


class Caribbean(Locale):
    _iso_code = '029'
    english_name = 'Caribbean'
    _flag = None
    languages = [
        English(u'Caribbean', lcid=0x0009)
    ]


class CaribbeanNetherlands(Locale):
    _iso_code = 'BQ'
    english_name = 'Caribbean Netherlands'
    _flag = 'flags\\BQ.png'
    languages = [
        Dutch(u'Caribisch Nederland', lcid=None)
    ]


class CaymanIslands(Locale):
    _iso_code = 'KY'
    english_name = 'Cayman Islands'
    _flag = 'flags\\KY.png'
    languages = [
        English(u'Cayman Islands', lcid=0x1000)
    ]


class CentralAfricanRepublic(Locale):
    _iso_code = 'CF'
    english_name = 'Central African Republic'
    _flag = 'flags\\CF.png'
    languages = [
        French(u'République Centrafricaine', lcid=None),
        Sango(u'Ködörösêse tî Bêafrîka', lcid=None),
        Lingala(u'', lcid=0x1000)
    ]


class Chad(Locale):
    _iso_code = 'TD'
    english_name = 'Chad'
    _flag = 'flags\\TD.png'
    languages = [
        Arabic(u'تشاد', lcid=None),
        French(u'Tchad', lcid=None)
    ]


class Chile(Locale):
    _iso_code = 'CL'
    english_name = 'Chile'
    _flag = 'flags\\CL.png'
    languages = [
        Spanish(u'Chile', lcid=0x340A),
        Mapudungun(u'', lcid=0x007A)
    ]


class China(Locale):
    _iso_code = 'CN'
    english_name = 'China (People\'s Republic Of)'
    _flag = 'flags\\CN.png'
    languages = [
        ChineseSimplified(u'中国 (中华人民共和国)', lcid=0x0804),
        MongolianTraditional(u'', lcid=0x0850),
        Tibetan(u'', lcid=0x0051),
        Uyghur(u'', lcid=0x0080),
        SichuanYi(u'', lcid=0x0078)
    ]


class ChristmasIsland(Locale):
    _iso_code = 'CX'
    english_name = 'Christmas Island'
    _flag = 'flags\\CX.png'
    languages = [
        English(u'Christmas Island', lcid=0x1000)
    ]


class CityoftheVatican(Locale):
    _iso_code = 'VA'
    english_name = 'City of the Vatican'
    _flag = 'flags\\VA.png'
    languages = [
        Italian(u'Città del Vaticano', lcid=None)
    ]


class CocosIslands(Locale):
    _iso_code = 'CC'
    english_name = 'Cocos (Keeling) Islands'
    _flag = 'flags\\CC.png'
    languages = [
        English(u'Cocos (Keeling) Islands', lcid=0x1000)
    ]


class Colombia(Locale):
    _iso_code = 'CO'
    english_name = 'Colombia'
    _flag = 'flags\\CO.png'
    languages = [
        Spanish(u'Colombia', lcid=0x240A)
    ]


class Comores(Locale):
    _iso_code = 'KM'
    english_name = 'Comores'
    _flag = 'flags\\KM.png'
    languages = [
        Arabic(u'جزر القمر', lcid=None),
        French(u'Comores', lcid=None),
        Swahili(u'Komori', lcid=None)
    ]


class CookIslands(Locale):
    _iso_code = 'CK'
    english_name = 'Cook Islands'
    _flag = 'flags\\CK.png'
    languages = [
        English(u'Cook Islands', lcid=0x1000),
        Rarotongan(u'Kūki ʻĀirani', lcid=None)
    ]


class CostaRica(Locale):
    _iso_code = 'CR'
    english_name = 'Costa Rica'
    _flag = 'flags\\CR.png'
    languages = [
        Spanish(u'Costa Rica', lcid=0x140A)
    ]


class CountryOfNauru(Locale):
    _iso_code = 'NR'
    english_name = 'Nauru'
    _flag = 'flags\\NR.png'
    languages = [
        English(u'Nauru', lcid=0x1000),
        Nauru(u'', lcid=None)
    ]


class Croatia(Locale):
    _iso_code = 'HR'
    english_name = 'Croatia'
    _flag = 'flags\\HR.png'
    languages = [
        CroatianLatin(u'Hrvatska', lcid=0x041A)
    ]


class Cuba(Locale):
    _iso_code = 'CU'
    english_name = 'Cuba'
    _flag = 'flags\\CU.png'
    languages = [
        Spanish(u'Cuba', lcid=None)
    ]


class Curacao(Locale):
    _iso_code = 'CW'
    english_name = 'Curacao'
    _flag = 'flags\\CW.png'
    languages = [
        English(u'Curacao', lcid=0x1000),
        Dutch(u'Curaçao', lcid=None)
    ]


class Cyprus(Locale):
    _iso_code = 'CY'
    english_name = 'Cyprus'
    _flag = 'flags\\CY.png'
    languages = [
        Greek(u'Κύπρος', lcid=None),
        Turkish(u'Kıbrıs', lcid=None),
        English(u'Cyprus', lcid=0x0009)
    ]


class CzechRepublic(Locale):
    _iso_code = 'CZ'
    english_name = 'Czech Republic'
    _flag = 'flags\\CZ.png'
    languages = [
        Czech(u'Česká republika Česko', lcid=0x0405)
    ]


class DemocraticRepublicCongo(Locale):
    _iso_code = 'CD'
    english_name = 'Democratic Republic of the Congo'
    _flag = 'flags\\CD.png'
    languages = [
        French(u'République démocratique du Congo', lcid=None),
        CongoSwahili(u'Jamhuri ya Kidemokrasia ya Kongo', lcid=0x1000),
        Lingala(u'Republíki ya Kongó Demokratíki', lcid=0x1000),
        LubaKatanga(u'', lcid=0x1000)
    ]


class Denmark(Locale):
    _iso_code = 'DK'
    english_name = 'Denmark'
    _flag = 'flags\\DK.png'
    languages = [
        Danish(u'Danmark', lcid=0x0406),
        English(u'Denmark', lcid=0x0009),
        Faroese(u'', lcid=0x0038)
    ]


class Djibouti(Locale):
    _iso_code = 'DJ'
    english_name = 'Djibouti'
    _flag = 'flags\\DJ.png'
    languages = [
        Afar(u'Gabuutih', lcid=None),
        Arabic(u'جيبوتي', lcid=None),
        French(u'Djibouti', lcid=None),
        Somali(u'Jabuuti', lcid=None)
    ]


class Dominica(Locale):
    _iso_code = 'DM'
    english_name = 'Dominica'
    _flag = 'flags\\DM.png'
    languages = [
        English(u'Dominica', lcid=0x1000)
    ]


class DominicanRepublic(Locale):
    _iso_code = 'DO'
    english_name = 'Dominican Republic'
    _flag = 'flags\\DO.png'
    languages = [
        Spanish(u'República Dominicana', lcid=0x1C0A)
    ]


class Ecuador(Locale):
    _iso_code = 'EC'
    english_name = 'Ecuador'
    _flag = 'flags\\EC.png'
    languages = [
        Spanish(u'Ecuador', lcid=0x300A),
        Quechua(u'', lcid=0x006B)
    ]


class Egypt(Locale):
    _iso_code = 'EG'
    english_name = 'Egypt'
    _flag = 'flags\\EG.png'
    languages = [
        Arabic(u'مصر', lcid=0x0C01)
    ]


class ElSalvador(Locale):
    _iso_code = 'SV'
    english_name = 'El Salvador'
    _flag = 'flags\\SV.png'
    languages = [
        Spanish(u'El Salvador', lcid=0x440A)
    ]


class EquatorialGuinea(Locale):
    _iso_code = 'GQ'
    english_name = 'Equatorial Guinea'
    _flag = 'flags\\GQ.png'
    languages = [
        Spanish(u'Guiena ecuatorial', lcid=None),
        French(u'Guinée équatoriale', lcid=None),
        Portuguese(u'Guiné Equatorial', lcid=None)
    ]


class Eritrea(Locale):
    _iso_code = 'ER'
    english_name = 'Eritrea'
    _flag = 'flags\\ER.png'
    languages = [
        Arabic(u'إرتريا', lcid=None),
        English(u'Eritrea', lcid=0x1000),
        Tigrinya(u'ኤርትራ', lcid=None),
        Afar(u'', lcid=0x1000),
        Blin(u'', lcid=0x1000),
        Saho(u'', lcid=0x1000),
        Tigre(u'', lcid=0x1000)
    ]


class Estonia(Locale):
    _iso_code = 'EE'
    english_name = 'Estonia'
    _flag = 'flags\\EE.png'
    languages = [
        Estonian(u'eSwatini', lcid=0x0425)
    ]


class Ethiopia(Locale):
    _iso_code = 'ET'
    english_name = 'Ethiopia'
    _flag = 'flags\\ET.png'
    languages = [
        Amharic(u'ኢትዮጵያ', lcid=0x045E),
        Oromo(u'Itoophiyaa', lcid=None),
        Afar(u'', lcid=0x1000),
        Somali(u'', lcid=0x0077),
        Tigrinya(u'', lcid=0x0073),
        Walamo(u'', lcid=0x1000)
    ]


class FalklandIslands(Locale):
    _iso_code = 'FK'
    english_name = 'Falkland Islands'
    _flag = 'flags\\FK.png'
    languages = [
        English(u'Falkland Islands', lcid=0x1000)
    ]


class FaroeIslands(Locale):
    _iso_code = 'FO'
    english_name = 'Faroe Islands'
    _flag = 'flags\\FO.png'
    languages = [
        Danish(u'Færøerne', lcid=None),
        Faroese(u'Føroyar', lcid=0x0438)
    ]


class Fiji(Locale):
    _iso_code = 'FJ'
    english_name = 'Fiji'
    _flag = 'flags\\FJ.png'
    languages = [
        English(u'Fiji', lcid=0x1000)
    ]


class Finland(Locale):
    _iso_code = 'FI'
    english_name = 'Finland'
    _flag = 'flags\\FI.png'
    languages = [
        Finnish(u'Suomi', lcid=0x040B),
        SamiNorthern(u'Suopma', lcid=0x0C3B),
        Swedish(u'Finland', lcid=0x081D),
        English(u'Finland', lcid=0x0009),
        SamiInari(u'', lcid=0x703B),
        SamiSkolt(u'', lcid=0x743B)
    ]


class France(Locale):
    _iso_code = 'FR'
    english_name = 'France'
    _flag = 'flags\\FR.png'
    languages = [
        French(u'France', lcid=0x040C),
        SwissGerman(u'', lcid=0x0084),
        Breton(u'', lcid=0x007E),
        Catalan(u'', lcid=0x0003),
        Corsican(u'', lcid=0x0083),
        Interlingua(u'', lcid=0x1000),
        Occitan(u'', lcid=0x0082)
    ]


class FrenchGuiana(Locale):
    _iso_code = 'GF'
    english_name = 'French Guiana'
    _flag = 'flags\\GF.png'
    languages = [
        French(u'Guyane', lcid=None)
    ]


class FrenchPolynesia(Locale):
    _iso_code = 'PF'
    english_name = 'French Polynesia'
    _flag = 'flags\\PF.png'
    languages = [
        French(u'Polynésie française', lcid=None)
    ]


class FrenchSouthernandAntarcticLands(Locale):
    _iso_code = 'TF'
    english_name = 'French Southern and Antarctic Lands'
    _flag = 'flags\\TF.png'
    languages = [
        French(u'Terres australes et antarctiques françaises', lcid=None)
    ]


class Gabon(Locale):
    _iso_code = 'GA'
    english_name = 'Gabon'
    _flag = 'flags\\GA.png'
    languages = [
        French(u'République gabonaise', lcid=None)
    ]


class Georgia(Locale):
    _iso_code = 'GE'
    english_name = 'Georgia'
    _flag = 'flags\\GE.png'
    languages = [
        Georgian(u'საქართველო', lcid=0x0437),
        Ossetian(u'', lcid=0x1000)
    ]


class Germany(Locale):
    _iso_code = 'DE'
    english_name = 'Germany'
    _flag = 'flags\\DE.png'
    languages = [
        German(u'Deutschland', lcid=0x0407),
        Luxembourgish(u'Däitschland', lcid=None),
        SwissGerman(u'Deutschland', lcid=None),
        Bavarian(u'Deitschland', lcid=None),
        Danish(u'Tyskland', lcid=None),
        UpperSorbian(u'Nىmska', lcid=0x042E),
        LowerSorbian(u'Nimce', lcid=0x082E),
        NorthFrisian(u'Tjüschlönj', lcid=None),
        SaterlandFrisian(u'Dútslân', lcid=None),
        Romani(u'Jermaniya', lcid=None),
        LowGerman(u'Düütschland', lcid=None),
        English(u'Germany', lcid=0x1000),
        Ripuarian(u'', lcid=0x1000)
    ]


class Ghana(Locale):
    _iso_code = 'GH'
    english_name = 'Ghana'
    _flag = 'flags\\GH.png'
    languages = [
        English(u'Ghana', lcid=0x1000),
        Akan(u'Gaana', lcid=0x1000),
        Ewe(u'Gana', lcid=0x1000),
        HausaLatin(u'', lcid=0x1000)
    ]


class Gibraltar(Locale):
    _iso_code = 'GI'
    english_name = 'Gibraltar'
    _flag = 'flags\\GI.png'
    languages = [
        English(u'Gibraltar', lcid=0x1000)
    ]


class Greece(Locale):
    _iso_code = 'GR'
    english_name = 'Greece'
    _flag = 'flags\\GR.png'
    languages = [
        Greek(u'Ελλάδα', lcid=0x0408)
    ]


class Greenland(Locale):
    _iso_code = 'GL'
    english_name = 'Greenland'
    _flag = 'flags\\GL.png'
    languages = [
        Danish(u'Grønland', lcid=None),
        Kalaallisut(u'Kalaallit Nunaat', lcid=0x046F)
    ]


class Grenada(Locale):
    _iso_code = 'GD'
    english_name = 'Grenada'
    _flag = 'flags\\GD.png'
    languages = [
        English(u'Grenada', lcid=0x1000)
    ]


class Guadeloupe(Locale):
    _iso_code = 'GP'
    english_name = 'Guadeloupe'
    _flag = 'flags\\GP.png'
    languages = [
        French(u'Guadeloupe', lcid=None)
    ]


class Guam(Locale):
    _iso_code = 'GU'
    english_name = 'Guam'
    _flag = 'flags\\GU.png'
    languages = [
        Chamorro(u'Guåhån', lcid=None),
        English(u'Guam', lcid=0x1000)
    ]


class Guatemala(Locale):
    _iso_code = 'GT'
    english_name = 'Guatemala'
    _flag = 'flags\\GT.png'
    languages = [
        Spanish(u'Guatemala', lcid=0x100A),
        Kiche(u'', lcid=0x0486)
    ]


class Guernsey(Locale):
    _iso_code = 'GG'
    english_name = 'Guernsey'
    _flag = 'flags\\GG.png'
    languages = [
        English(u'Guernsey', lcid=0x1000)
    ]


class Guinea(Locale):
    _iso_code = 'GN'
    english_name = 'Guinea'
    _flag = 'flags\\GN.png'
    languages = [
        French(u'Guinée', lcid=None),
        Fulah(u'Gine', lcid=0x0067),
        Nko(u'', lcid=0x1000)
    ]


class GuineaBissau(Locale):
    _iso_code = 'GW'
    english_name = 'Guinea Bissau'
    _flag = 'flags\\GW.png'
    languages = [
        Portuguese(u'Guiné-Bissau', lcid=None)
    ]


class Guyana(Locale):
    _iso_code = 'GY'
    english_name = 'Guyana'
    _flag = 'flags\\GY.png'
    languages = [
        English(u'Guyana', lcid=0x1000)
    ]


class Haiti(Locale):
    _iso_code = 'HT'
    english_name = 'Haiti'
    _flag = 'flags\\HT.png'
    languages = [
        French(u'Haïti', lcid=None),
        HaitianCreole(u'Ayiti', lcid=None)
    ]


class HeardIslandandMcDonaldIslands(Locale):
    _iso_code = 'HM'
    english_name = 'Heard Island and McDonald Islands'
    _flag = 'flags\\HM.png'
    languages = [
        English(u'Heard Island and McDonald Islands', lcid=0x1000)
    ]


class Honduras(Locale):
    _iso_code = 'HN'
    english_name = 'Honduras'
    _flag = 'flags\\HN.png'
    languages = [
        Spanish(u'Honduras', lcid=0x480A)
    ]


class HongKong(Locale):
    _iso_code = 'HK'
    english_name = 'Hong Kong (SAR of China)'
    _flag = 'flags\\HK.png'
    languages = [
        English(u'Hong Kong', lcid=0x1000),
        ChineseTraditional(u'香港', lcid=None)
    ]


class Hungary(Locale):
    _iso_code = 'HU'
    english_name = 'Hungary'
    _flag = 'flags\\HU.png'
    languages = [
        Hungarian(u'Magyarország', lcid=0x040E)
    ]


class Iceland(Locale):
    _iso_code = 'IS'
    english_name = 'Iceland'
    _flag = 'flags\\IS.png'
    languages = [
        Icelandic(u'Ísland', lcid=0x040F)
    ]


class India(Locale):
    _iso_code = 'IN'
    english_name = 'India'
    _flag = 'flags\\IN.png'
    languages = [
        English(u'India', lcid=0x4009),
        Hindi(u'भारत', lcid=0x0439),
        Assamese(u'ভাৰত', lcid=0x004D),
        Bengali(u'ভারত', lcid=0x0045),
        Bodo(u'', lcid=0x1000),
        Gujarati(u'ભારત', lcid=0x0047),
        Kannada(u'ಭಾರತ', lcid=0x004B),
        Kashmiri(u'', lcid=0x1000),
        Konkani(u'भारत', lcid=0x0057),
        Malayalam(u'ഭാരതം', lcid=0x004C),
        Marathi(u'भारत', lcid=0x004E),
        Nepali(u'भारत', lcid=0x0061),
        Oriya(u'ଭାରତ', lcid=0x0048),
        Punjabi(u'ਭਾਰਤ', lcid=0x0046),
        Sanskrit(u'भारतम्', lcid=0x004F),
        Tamil(u'பாரதம்', lcid=0x0049),
        Telugu(u'భారత దేశం', lcid=0x004A),
        Tibetan(u'', lcid=0x0051),
        Urdu(u'', lcid=0x0020)
    ]


class Indonesia(Locale):
    _iso_code = 'ID'
    english_name = 'Indonesia'
    _flag = 'flags\\ID.png'
    languages = [
        Indonesian(u'Indonesia', lcid=0x0421),
        Javanese(u'', lcid=0x1000)
    ]


class Iran(Locale):
    _iso_code = 'IR'
    english_name = 'Iran'
    _flag = 'flags\\IR.png'
    languages = [
        Persian(u'ایران', lcid=0x0429),
        Kurdish(u'', lcid=0x0492),
        Mazanderani(u'', lcid=0x1000),
        NorthernLuri(u'', lcid=0x1000)
    ]


class Iraq(Locale):
    _iso_code = 'IQ'
    english_name = 'Iraq'
    _flag = 'flags\\IQ.png'
    languages = [
        Arabic(u'العراق', lcid=0x0801),
        Kurdish(u'Îraq', lcid=None),
        CentralKurdish(u'', lcid=0x0492),
        NorthernLuri(u'', lcid=0x1000)
    ]


class Ireland(Locale):
    _iso_code = 'IE'
    english_name = 'Ireland'
    _flag = 'flags\\IE.png'
    languages = [
        English(u'Ireland', lcid=0x1809),
        Irish(u'Éire', lcid=0x083C)
    ]


class IsleofMan(Locale):
    _iso_code = 'IM'
    english_name = 'Isle of Man'
    _flag = 'flags\\IM.png'
    languages = [
        English(u'Isle of Man', lcid=0x1000),
        Manx(u'Ellan Vannin', lcid=0x1000)
    ]


class Israel(Locale):
    _iso_code = 'IL'
    english_name = 'Israel'
    _flag = 'flags\\IL.png'
    languages = [
        Hebrew(u'ישראל', lcid=0x040D),
        Arabic(u'إسرائيل', lcid=0x0001),
        English(u'Israel', lcid=0x0009)
    ]


class Italia(Locale):
    _iso_code = 'IT'
    english_name = 'Italia'
    _flag = 'flags\\IT.png'
    languages = [
        German(u'Italia', lcid=None),
        French(u'Italia', lcid=None),
        Italian(u'Italia', lcid=0x0410),
        Catalan(u'', lcid=0x0003),
        Friulian(u'', lcid=0x1000)
    ]


class IvoryCoast(Locale):
    _iso_code = 'CI'
    english_name = 'Ivory Coast'
    _flag = 'flags\\CI.png'
    languages = [
        French(u'Côte d\'Ivoire', lcid=None)
    ]


class Jamaica(Locale):
    _iso_code = 'JM'
    english_name = 'Jamaica'
    _flag = 'flags\\JM.png'
    languages = [
        English(u'Jamaica', lcid=0x2009)
    ]


class Japan(Locale):
    _iso_code = 'JP'
    english_name = 'Japan'
    _flag = 'flags\\JP.png'
    languages = [
        Japanese(u'日本', lcid=0x0411)
    ]


class Jersey(Locale):
    _iso_code = 'JE'
    english_name = 'Jersey'
    _flag = 'flags\\JE.png'
    languages = [
        English(u'Jersey', lcid=0x1000)
    ]


class Jordan(Locale):
    _iso_code = 'JO'
    english_name = 'Jordan'
    _flag = 'flags\\JO.png'
    languages = [
        Arabic(u'الأردن', lcid=0x2C01)
    ]


class Kazakhstan(Locale):
    _iso_code = 'KZ'
    english_name = 'Kazakhstan'
    _flag = 'flags\\KZ.png'
    languages = [
        Kazakh(u'Қазақстан', lcid=0x043F),
        Russian(u'Казахстан', lcid=None)
    ]


class Kenya(Locale):
    _iso_code = 'KE'
    english_name = 'Kenya'
    _flag = 'flags\\KE.png'
    languages = [
        English(u'Kenya', lcid=0x1000),
        Swahili(u'Kenya', lcid=0x0441),
        Embu(u'', lcid=0x1000),
        Gusii(u'', lcid=0x1000),
        Kalenjin(u'', lcid=0x1000),
        Kamba(u'', lcid=0x1000),
        Kikuyu(u'', lcid=0x1000),
        Luo(u'', lcid=0x1000),
        Luyia(u'', lcid=0x1000),
        Masai(u'', lcid=0x1000),
        Meru(u'', lcid=0x1000),
        Oromo(u'', lcid=0x0072),
        Samburu(u'', lcid=0x1000),
        Somali(u'', lcid=0x0077),
        Taita(u'', lcid=0x1000),
        Teso(u'', lcid=0x1000)
    ]


class Kiribati(Locale):
    _iso_code = 'KI'
    english_name = 'Kiribati'
    _flag = 'flags\\KI.png'
    languages = [
        English(u'Kiribati', lcid=0x1000)
    ]


class Kuweit(Locale):
    _iso_code = 'KW'
    english_name = 'Kuweit'
    _flag = 'flags\\KW.png'
    languages = [
        Arabic(u'دولة الكويت', lcid=0x3401)
    ]


class Kyrgyzstan(Locale):
    _iso_code = 'KG'
    english_name = 'Kyrgyzstan'
    _flag = 'flags\\KG.png'
    languages = [
        Kyrgyz(u'Кыргызстан', lcid=0x0440),
        Russian(u'Киргизия', lcid=None)
    ]


class Laos(Locale):
    _iso_code = 'LA'
    english_name = 'Laos'
    _flag = 'flags\\LA.png'
    languages = [
        Lao(u'ປະເທດລາວ', lcid=0x0454)
    ]


class LatinAmerica(Locale):
    _iso_code = '419'
    english_name = 'Latin America'
    _flag = None
    languages = [
        Spanish(u'', lcid=0x000A)
    ]


class Latvia(Locale):
    _iso_code = 'LV'
    english_name = 'Latvia'
    _flag = 'flags\\LV.png'
    languages = [
        Latvian(u'Latvija', lcid=0x0426)
    ]


class Lebanon(Locale):
    _iso_code = 'LB'
    english_name = 'Lebanon'
    _flag = 'flags\\LB.png'
    languages = [
        Arabic(u'لبنان', lcid=0x3001),
        French(u'Liban', lcid=None)
    ]


class Lesotho(Locale):
    _iso_code = 'LS'
    english_name = 'Lesotho'
    _flag = 'flags\\LS.png'
    languages = [
        English(u'Lesotho', lcid=0x1000),
        Sotho(u'Lesotho', lcid=None),
        SothoSouthern(u'', lcid=0x0030)
    ]


class Liberia(Locale):
    _iso_code = 'LR'
    english_name = 'Liberia'
    _flag = 'flags\\LR.png'
    languages = [
        English(u'Liberia', lcid=0x1000),
        Vai(u'', lcid=0x1000),
        VaiLatin(u'', lcid=0x1000)
    ]


class Libya(Locale):
    _iso_code = 'LY'
    english_name = 'Libya'
    _flag = 'flags\\LY.png'
    languages = [
        Arabic(u'ليبيا', lcid=0x1001)
    ]


class Liechtenstein(Locale):
    _iso_code = 'LI'
    english_name = 'Liechtenstein'
    _flag = 'flags\\LI.png'
    languages = [
        German(u'Liechtenstein', lcid=0x1407),
        SwissGerman(u'', lcid=0x0084)
    ]


class Lithuania(Locale):
    _iso_code = 'LT'
    english_name = 'Lithuania'
    _flag = 'flags\\LT.png'
    languages = [
        Lithuanian(u'Lietuva', lcid=0x0427)
    ]


class Luxembourg(Locale):
    _iso_code = 'LU'
    english_name = 'Luxembourg'
    _flag = 'flags\\LU.png'
    languages = [
        German(u'Luxemburg', lcid=0x1007),
        French(u'Luxembourg', lcid=0x140C),
        Luxembourgish(u'Lëtzebuerg', lcid=0x046E),
        Portuguese(u'', lcid=0x0016)
    ]


class Macau(Locale):
    _iso_code = 'MO'
    english_name = 'Macau (SAR of China)'
    _flag = 'flags\\MO.png'
    languages = [
        Portuguese(u'Macau', lcid=None),
        ChineseTraditional(u'澳門', lcid=None),
        English(u'Macau', lcid=0x0009)
    ]


class Macedonia(Locale):
    _iso_code = 'MK'
    english_name = 'Macedonia (Former Yugoslav Republic of)'
    _flag = 'flags\\MK.png'
    languages = [
        Macedonian(u'Македонија', lcid=0x042F),
        Albanian(u'', lcid=0x001C)
    ]


class Madagascar(Locale):
    _iso_code = 'MG'
    english_name = 'Madagascar'
    _flag = 'flags\\MG.png'
    languages = [
        French(u'Madagascar', lcid=None),
        Malagasy(u'Madagasikara', lcid=None),
        English(u'Madagascar', lcid=0x0009)
    ]


class Malawi(Locale):
    _iso_code = 'MW'
    english_name = 'Malawi'
    _flag = 'flags\\MW.png'
    languages = [
        English(u'Malawi', lcid=0x1000),
        Nyanja(u'Malaŵi', lcid=None)
    ]


class Malaysia(Locale):
    _iso_code = 'MY'
    english_name = 'Malaysia'
    _flag = 'flags\\MY.png'
    languages = [
        Malay(u'Malaysia', lcid=0x043E),
        English(u'Malaysia', lcid=0x0009),
        Tamil(u'மலேசியா', lcid=0x0049)
    ]


class Maldives(Locale):
    _iso_code = 'MV'
    english_name = 'Maldives'
    _flag = 'flags\\MV.png'
    languages = [
        Divehi(u'ދިވެހިރާއްޖެ', lcid=0x0465)
    ]


class Mali(Locale):
    _iso_code = 'ML'
    english_name = 'Mali'
    _flag = 'flags\\ML.png'
    languages = [
        French(u'Mali', lcid=None),
        BamanankanLatin(u'', lcid=0x1000),
        KoyraChiini(u'', lcid=0x1000),
        KoyraboroSenni(u'', lcid=0x1000)
    ]


class Malta(Locale):
    _iso_code = 'MT'
    english_name = 'Malta'
    _flag = 'flags\\MT.png'
    languages = [
        English(u'Malta', lcid=0x1000),
        Maltese(u'Malta', lcid=0x043A)
    ]


class MarshallIslands(Locale):
    _iso_code = 'MH'
    english_name = 'Marshall Islands'
    _flag = 'flags\\MH.png'
    languages = [
        English(u'Marshall Islands', lcid=0x1000),
        Marshallese(u'Aorōkin M̧ajeļ', lcid=None)
    ]


class Martinique(Locale):
    _iso_code = 'MQ'
    english_name = 'Martinique'
    _flag = 'flags\\MQ.png'
    languages = [
        French(u'Martinique', lcid=None)
    ]


class Mauritania(Locale):
    _iso_code = 'MR'
    english_name = 'Mauritania'
    _flag = 'flags\\MR.png'
    languages = [
        Arabic(u'موريتانيا', lcid=None),
        French(u'Mauritanie', lcid=None),
        Fulah(u'ⵎⵓⵔⵉⵜⴰⵏ / ⴰⴳⴰⵡⵛ', lcid=0x0067)
    ]


class Mauritius(Locale):
    _iso_code = 'MU'
    english_name = 'Mauritius'
    _flag = 'flags\\MU.png'
    languages = [
        English(u'Mauritius', lcid=0x1000),
        French(u'Maurice', lcid=None),
        Morisyen(u'Moris', lcid=None)
    ]


class Mayotte(Locale):
    _iso_code = 'YT'
    english_name = 'Mayotte'
    _flag = 'flags\\YT.png'
    languages = [
        French(u'Mayotte', lcid=None)
    ]


class Mexico(Locale):
    _iso_code = 'MX'
    english_name = 'Mexico'
    _flag = 'flags\\MX.png'
    languages = [
        Spanish(u'México', lcid=0x080A)
    ]


class Micronesia(Locale):
    _iso_code = 'FM'
    english_name = 'Micronesia (Federated States of)'
    _flag = 'flags\\FM.png'
    languages = [
        English(u'Micronesia', lcid=0x1000)
    ]


class Moldova(Locale):
    _iso_code = 'MD'
    english_name = 'Moldova'
    _flag = 'flags\\MD.png'
    languages = [
        Romanian(u'Moldova', lcid=None),
        Russian(u'Молдавия', lcid=None),
        Ukrainian(u'Молдова', lcid=None)
    ]


class Monaco(Locale):
    _iso_code = 'MC'
    english_name = 'Monaco'
    _flag = 'flags\\MC.png'
    languages = [
        French(u'Monaco', lcid=0x180C)
    ]


class Mongolia(Locale):
    _iso_code = 'MN'
    english_name = 'Mongolia'
    _flag = 'flags\\MN.png'
    languages = [
        Mongolian(u'ᠮᠤᠩᠭᠤᠯ ᠤᠯᠤᠰ', lcid=0x0450)
    ]


class Montenegro(Locale):
    _iso_code = 'ME'
    english_name = 'Montenegro'
    _flag = 'flags\\ME.png'
    languages = [
        BosnianCyrillic(u'Crna Gora', lcid=None),
        CroatianLatin(u'Crna Gora', lcid=None),
        Albanian(u'Mali i Zi', lcid=None),
        SerbianCyrillic(u'Црна Гора', lcid=None),
        SerbianLatin(u'', lcid=0x181A)
    ]


class Montserrat(Locale):
    _iso_code = 'MS'
    english_name = 'Montserrat'
    _flag = 'flags\\MS.png'
    languages = [
        English(u'Montserrat', lcid=0x1000)
    ]


class Morocco(Locale):
    _iso_code = 'MA'
    english_name = 'Morocco'
    _flag = 'flags\\MA.png'
    languages = [
        Arabic(u'المغرب', lcid=0x1801),
        French(u'Maroc', lcid=None),
        StandardMoroccanTamazight(u'ⴰⵎⵔⵔⵓⴽ / ⵍⵎⵖⵔⵉⴱ', lcid=None),
        CentralAtlasTamazightLatin(u'', lcid=0x1000),
        Tachelhit(u'', lcid=0x1000),
        TachelhitLatin(u'', lcid=0x1000)
    ]


class Mozambique(Locale):
    _iso_code = 'MZ'
    english_name = 'Mozambique'
    _flag = 'flags\\MZ.png'
    languages = [
        Portuguese(u'Moçambique', lcid=None),
        MakhuwaMeetto(u'', lcid=0x1000),
        Sena(u'', lcid=0x1000)
    ]


class Myanmar(Locale):
    _iso_code = 'MM'
    english_name = 'Myanmar'
    _flag = 'flags\\MM.png'
    languages = [
        Burmese(u'မြန်မာ', lcid=None)
    ]


class Namibia(Locale):
    _iso_code = 'NA'
    english_name = 'Namibia'
    _flag = 'flags\\NA.png'
    languages = [
        German(u'Namibia', lcid=None),
        English(u'Namibia', lcid=0x1000),
        Afrikaans(u'Namibia', lcid=0x0036),
        Nama(u'Namibia', lcid=0x1000)
    ]


class Nepal(Locale):
    _iso_code = 'NP'
    english_name = 'Nepal'
    _flag = 'flags\\NP.png'
    languages = [
        Nepali(u'Nepāl', lcid=0x0461)
    ]


class NewCaledonia(Locale):
    _iso_code = 'NC'
    english_name = 'New Caledonia'
    _flag = 'flags\\NC.png'
    languages = [
        French(u'Nouvelle-Calédonie', lcid=None)
    ]


class NewZealand(Locale):
    _iso_code = 'NZ'
    english_name = 'New Zealand'
    _flag = 'flags\\NZ.png'
    languages = [
        English(u'New Zealand', lcid=0x1409),
        Maori(u'Aotearoa', lcid=0x0481)
    ]


class Nicaragua(Locale):
    _iso_code = 'NI'
    english_name = 'Nicaragua'
    _flag = 'flags\\NI.png'
    languages = [
        Spanish(u'Nicaragua', lcid=0x4C0A)
    ]


class Niger(Locale):
    _iso_code = 'NE'
    english_name = 'Niger'
    _flag = 'flags\\NE.png'
    languages = [
        French(u'Niger', lcid=None),
        HausaLatin(u'', lcid=0x1000),
        Tasawaq(u'', lcid=0x1000),
        Zarma(u'', lcid=0x1000)
    ]


class Nigeria(Locale):
    _iso_code = 'NG'
    english_name = 'Nigeria'
    _flag = 'flags\\NG.png'
    languages = [
        English(u'Nigeria', lcid=0x1000),
        HausaLatin(u'Nijeriya ', lcid=0x1000),
        Igbo(u'Naigeria', lcid=0x0070),
        Yoruba(u'Nàìjíríà', lcid=0x006A)
    ]


class Niue(Locale):
    _iso_code = 'NU'
    english_name = 'Niue'
    _flag = 'flags\\NU.png'
    languages = [
        English(u'Niue', lcid=0x1000),
        Niuean(u'Niuē', lcid=None)
    ]


class NorfolkIsland(Locale):
    _iso_code = 'NF'
    english_name = 'Norfolk Island'
    _flag = 'flags\\NF.png'
    languages = [
        English(u'Norfolk Island', lcid=0x1000),
        PitcairnNorfolk(u'Norf\'k Ailen', lcid=None)
    ]


class NorthKorea(Locale):
    _iso_code = 'KP'
    english_name = 'North Korea'
    _flag = 'flags\\KP.png'
    languages = [
        Korean(u'북조선', lcid=None)
    ]


class NorthernMarianaIslands(Locale):
    _iso_code = 'MP'
    english_name = 'Northern Mariana Islands'
    _flag = 'flags\\MP.png'
    languages = [
        Chamorro(u'Notte Mariånas', lcid=None),
        English(u'Northern Mariana Islands', lcid=0x1000)
    ]


class Norway(Locale):
    _iso_code = 'NO'
    english_name = 'Norway'
    _flag = 'flags\\NO.png'
    languages = [
        NorwegianBokmal(u'Norge', lcid=0x0414),
        NorwegianNynorsk(u'Noreg', lcid=0x0814),
        Norwegian(u'Norge', lcid=None),
        SamiNorthern(u'Norga', lcid=0x043B),
        SamiLule(u'', lcid=0x7C3B),
        SamiSouthern(u'', lcid=0x783B)
    ]


class Oman(Locale):
    _iso_code = 'OM'
    english_name = 'Oman'
    _flag = 'flags\\OM.png'
    languages = [
        Arabic(u'عُمان', lcid=0x2001)
    ]


class Pakistan(Locale):
    _iso_code = 'PK'
    english_name = 'Pakistan'
    _flag = 'flags\\PK.png'
    languages = [
        English(u'Pakistan', lcid=0x1000),
        Urdu(u'Pākistān', lcid=0x0420),
        Punjabi(u'', lcid=0x0846),
        Sindhi(u'', lcid=0x0859)
    ]


class Palau(Locale):
    _iso_code = 'PW'
    english_name = 'Palau'
    _flag = 'flags\\PW.png'
    languages = [
        English(u'Palau', lcid=0x1000),
        Japanese(u'パラオ', lcid=None),
        Palauan(u'Belau', lcid=None),
        Tobian(u'Palau', lcid=None)
    ]


class PalestinianTerritory(Locale):
    _iso_code = 'PS'
    english_name = 'Palestinian Territory'
    _flag = 'flags\\PS.png'
    languages = [
        Arabic(u'فلسطين', lcid=None),
        Hebrew(u'טריטוריה פלסטינית', lcid=None)
    ]


class Panama(Locale):
    _iso_code = 'PA'
    english_name = 'Panama'
    _flag = 'flags\\PA.png'
    languages = [
        Spanish(u'Panamá', lcid=0x180A)
    ]


class PapuaNewGuinea(Locale):
    _iso_code = 'PG'
    english_name = 'Papua New Guinea'
    _flag = 'flags\\PG.png'
    languages = [
        English(u'Papua New Guinea', lcid=0x1000),
        HiriMotu(u'Papua Niugini', lcid=None),
        TokPisin(u'Papua Niugini', lcid=None)
    ]


class Paraguay(Locale):
    _iso_code = 'PY'
    english_name = 'Paraguay'
    _flag = 'flags\\PY.png'
    languages = [
        Spanish(u'Paraguay', lcid=0x3C0A),
        Guarani(u'Paraguái', lcid=None)
    ]


class Peru(Locale):
    _iso_code = 'PE'
    english_name = 'Peru'
    _flag = 'flags\\PE.png'
    languages = [
        Spanish(u'Perú', lcid=0x280A),
        Quechua(u'Piruw', lcid=0x006B)
    ]


class Philippines(Locale):
    _iso_code = 'PH'
    english_name = 'Philippines'
    _flag = 'flags\\PH.png'
    languages = [
        English(u'Philippines', lcid=0x3409),
        Tagalog(u'', lcid=None),
        Filipino(u'Pilipinas', lcid=0x0064),
        Spanish(u'', lcid=0x000A)
    ]


class Pitcairn(Locale):
    _iso_code = 'PN'
    english_name = 'Pitcairn'
    _flag = 'flags\\PN.png'
    languages = [
        English(u'Pitcairn', lcid=0x1000),
        PitcairnNorfolk(u'Pitkern Ailen', lcid=None)
    ]


class Poland(Locale):
    _iso_code = 'PL'
    english_name = 'Poland'
    _flag = 'flags\\PL.png'
    languages = [
        Polish(u'Polska', lcid=0x0415)
    ]


class Portugal(Locale):
    _iso_code = 'PT'
    english_name = 'Portugal'
    _flag = 'flags\\PT.png'
    languages = [
        Portuguese(u'Portugal', lcid=0x0816)
    ]


class PuertoRico(Locale):
    _iso_code = 'PR'
    english_name = 'Puerto Rico'
    _flag = 'flags\\PR.png'
    languages = [
        English(u'Puerto Rico', lcid=0x1000),
        Spanish(u'Puerto Rico', lcid=0x500A)
    ]


class Qatar(Locale):
    _iso_code = 'QA'
    english_name = 'Qatar'
    _flag = 'flags\\QA.png'
    languages = [
        Arabic(u'قطر', lcid=0x4001)
    ]


class RepublicCongo(Locale):
    _iso_code = 'CG'
    english_name = 'Republic of the Congo (Congo-Brazzaville)'
    _flag = 'flags\\CG.png'
    languages = [
        French(u'République démocratique du Congo', lcid=None),
        Lingala(u'Republíki ya Kongó Demokratíki', lcid=0x1000)
    ]


class Reunion(Locale):
    _iso_code = 'RE'
    english_name = 'Reunion'
    _flag = 'flags\\RE.png'
    languages = [
        French(u'Réunion', lcid=None)
    ]


class Romania(Locale):
    _iso_code = 'RO'
    english_name = 'Romania'
    _flag = 'flags\\RO.png'
    languages = [
        Romanian(u'România', lcid=0x0418)
    ]


class Russia(Locale):
    _iso_code = 'RU'
    english_name = 'Russia'
    _flag = 'flags\\RU.png'
    languages = [
        Russian(u'Россия', lcid=0x0419),
        Bashkir(u'', lcid=0x006D),
        Chechen(u'', lcid=0x1000),
        ChurchSlavic(u'', lcid=0x1000),
        Ossetian(u'', lcid=0x1000),
        Yakut(u'', lcid=0x0085),
        Tatar(u'', lcid=0x0044)
    ]


class Rwanda(Locale):
    _iso_code = 'RW'
    english_name = 'Rwanda'
    _flag = 'flags\\RW.png'
    languages = [
        English(u'Rwanda', lcid=0x1000),
        French(u'Rwanda', lcid=None),
        Kinyarwanda(u'Rwanda', lcid=0x0487)
    ]


class SaintBarts(Locale):
    _iso_code = 'BL'
    english_name = 'Saint-Barts'
    _flag = 'flags\\BL.png'
    languages = [
        French(u'Saint-Barthélemy', lcid=None)
    ]


class SaintHelena(Locale):
    _iso_code = 'SH'
    english_name = 'Saint Helena'
    _flag = 'flags\\SH.png'
    languages = [
        English(u'Saint Helena', lcid=0x1000)
    ]


class SaintKittsandNevis(Locale):
    _iso_code = 'KN'
    english_name = 'Saint Kitts and Nevis'
    _flag = 'flags\\KN.png'
    languages = [
        English(u'Saint Kitts and Nevis', lcid=0x1000)
    ]


class SaintLucia(Locale):
    _iso_code = 'LC'
    english_name = 'Saint Lucia'
    _flag = 'flags\\LC.png'
    languages = [
        English(u'Saint Lucia', lcid=0x1000)
    ]


class SaintMartinDutch(Locale):
    _iso_code = 'SX'
    english_name = 'Saint Martin (Dutch part)'
    _flag = 'flags\\SX.png'
    languages = [
        English(u'Saint Martin', lcid=0x1000),
        Dutch(u'Sint Maarten', lcid=None)
    ]


class SaintMartinFrench(Locale):
    _iso_code = 'MF'
    english_name = 'Saint Martin (French part)'
    _flag = 'flags\\MF.png'
    languages = [
        French(u'Saint-Martin', lcid=None)
    ]


class SaintPierreandMiquelon(Locale):
    _iso_code = 'PM'
    english_name = 'Saint Pierre and Miquelon'
    _flag = 'flags\\PM.png'
    languages = [
        French(u'Saint-Pierre et Miquelon', lcid=None)
    ]


class SaintVincentandtheGrenadines(Locale):
    _iso_code = 'VC'
    english_name = 'Saint Vincent and the Grenadines'
    _flag = 'flags\\VC.png'
    languages = [
        English(u'Saint Vincent and the Grenadines', lcid=0x1000)
    ]


class Samoa(Locale):
    _iso_code = 'WS'
    english_name = 'Samoa'
    _flag = 'flags\\WS.png'
    languages = [
        English(u'Samoa', lcid=0x1000),
        Samoan(u'Sāmoa', lcid=None)
    ]


class SanMarino(Locale):
    _iso_code = 'SM'
    english_name = 'San Marino'
    _flag = 'flags\\SM.png'
    languages = [
        Italian(u'San Marino', lcid=None)
    ]


class SaoTomeandPrincipe(Locale):
    _iso_code = 'ST'
    english_name = 'São Tomé and Príncipe'
    _flag = 'flags\\ST.png'
    languages = [
        Portuguese(u'São Tomé e Príncipe', lcid=None)
    ]


class SaudiArabia(Locale):
    _iso_code = 'SA'
    english_name = 'Saudi Arabia'
    _flag = 'flags\\SA.png'
    languages = [
        Arabic(u'المملكة العربية السعودية', lcid=0x0401)
    ]


class Senegal(Locale):
    _iso_code = 'SN'
    english_name = 'Senegal'
    _flag = 'flags\\SN.png'
    languages = [
        French(u'Sénégal', lcid=None),
        Fulah(u'', lcid=0x0867),
        JolaFonyi(u'', lcid=0x1000),
        Wolof(u'', lcid=0x0088)
    ]


class Serbia(Locale):
    _iso_code = 'RS'
    english_name = 'Serbia'
    _flag = 'flags\\RS.png'
    languages = [
        SerbianCyrillic(u'Србија', lcid=None),
        SerbianLatin(u'Srbija', lcid=0x181A)
    ]


class SerbiaMontenegro(Locale):
    _iso_code = 'CS'
    english_name = 'Serbia and Montenegro (Former)'
    _flag = None
    languages = [
        SerbianCyrillic(u'', lcid=0x1C1A),
        SerbianLatin(u'', lcid=0x181A)
    ]


class Seychelles(Locale):
    _iso_code = 'SC'
    english_name = 'Seychelles'
    _flag = 'flags\\SC.png'
    languages = [
        SeychelloisCreole(u'Sesel', lcid=None),
        English(u'Seychelles', lcid=0x1000),
        French(u'Seychelles', lcid=None)
    ]


class SierraLeone(Locale):
    _iso_code = 'SL'
    english_name = 'Sierra Leone'
    _flag = 'flags\\SL.png'
    languages = [
        English(u'Sierra Leone', lcid=0x1000)
    ]


class Singapore(Locale):
    _iso_code = 'SG'
    english_name = 'Singapore'
    _flag = 'flags\\SG.png'
    languages = [
        English(u'Singapore', lcid=0x4809),
        Malay(u'Singapura', lcid=None),
        Tamil(u'சிங்கப்பூர்', lcid=None),
        ChineseSimplified(u'新加坡', lcid=0x1004)
    ]


class Slovakia(Locale):
    _iso_code = 'SK'
    english_name = 'Slovakia'
    _flag = 'flags\\SK.png'
    languages = [
        Slovak(u'Slovensko', lcid=0x041B)
    ]


class Slovenia(Locale):
    _iso_code = 'SI'
    english_name = 'Slovenia'
    _flag = 'flags\\SI.png'
    languages = [
        Slovenian(u'Slovenija', lcid=0x0424),
        English(u'Slovenia', lcid=0x0009)
    ]


class SolomonIslands(Locale):
    _iso_code = 'SB'
    english_name = 'Solomon Islands'
    _flag = 'flags\\SB.png'
    languages = [
        English(u'Solomon Islands', lcid=0x1000)
    ]


class Somalia(Locale):
    _iso_code = 'SO'
    english_name = 'Somalia'
    _flag = 'flags\\SO.png'
    languages = [
        Arabic(u'الصومال', lcid=None),
        Somali(u'Soomaaliya', lcid=None)
    ]


class SouthAfrica(Locale):
    _iso_code = 'ZA'
    english_name = 'South Africa'
    _flag = 'flags\\ZA.png'
    languages = [
        Afrikaans(u'Suid-Afrika', lcid=0x0436),
        English(u'South Africa', lcid=0x1C09),
        Sotho(u'Afrika Borwa', lcid=None),
        Tswana(u'Aforika Borwa', lcid=0x0432),
        Xhosa(u'uMzantsi Afrika', lcid=0x0434),
        Zulu(u'iNingizimu Afrika', lcid=0x0435),
        SothoNorthern(u'Afrika Borwa', lcid=0x006C),
        SouthNdebele(u'iSewula Afrika', lcid=0x1000),
        Swati(u'iNingizimu Afrika', lcid=0x1000),
        Tsonga(u'Afrika Dzonga', lcid=0x0031),
        Venda(u'Afurika Tshipembe', lcid=0x0033)
    ]


class SouthGeorgiaandtheSouthSandwichIslands(Locale):
    _iso_code = 'GS'
    english_name = 'South Georgia and the South Sandwich Islands'
    _flag = 'flags\\GS.png'
    languages = [
        English(u'South Georgia and the South Sandwich Islands', lcid=0x1000)
    ]


class SouthKorea(Locale):
    _iso_code = 'KR'
    english_name = 'South Korea'
    _flag = 'flags\\KR.png'
    languages = [
        English(u'South Korea', lcid=0x1000),
        Korean(u'대한민국', lcid=0x0412)
    ]


class SouthSudan(Locale):
    _iso_code = 'SS'
    english_name = 'South Sudan'
    _flag = 'flags\\SS.png'
    languages = [
        English(u'South Sudan', lcid=0x1000),
        Arabic(u'', lcid=0x0001)
    ]


class Spain(Locale):
    _iso_code = 'ES'
    english_name = 'Spain'
    _flag = 'flags\\ES.png'
    languages = [
        Asturian(u'España', lcid=None),
        Catalan(u'Espanya', lcid=0x0403),
        Spanish(u'España', lcid=0x0C0A),
        Basque(u'Espainia', lcid=0x042D),
        Galician(u'España', lcid=0x0456)
    ]


class SriLanka(Locale):
    _iso_code = 'LK'
    english_name = 'Sri Lanka'
    _flag = 'flags\\LK.png'
    languages = [
        Sinhala(u'ශ්‍රී ලංකාව', lcid=0x045B),
        Tamil(u'இலங்கை', lcid=None)
    ]


class Sudan(Locale):
    _iso_code = 'SD'
    english_name = 'Sudan'
    _flag = 'flags\\SD.png'
    languages = [
        Arabic(u'السودان', lcid=None),
        English(u'Sudan', lcid=0x1000),
        Nuer(u'', lcid=0x1000)
    ]


class Suriname(Locale):
    _iso_code = 'SR'
    english_name = 'Suriname'
    _flag = 'flags\\SR.png'
    languages = [
        Dutch(u'Suriname', lcid=None)
    ]


class SvalbardandJanMayen(Locale):
    _iso_code = 'SJ'
    english_name = 'Svalbard and Jan Mayen'
    _flag = 'flags\\SJ.png'
    languages = [
        Norwegian(u'Svalbard og Jan Mayen', lcid=None),
        NorwegianBokmal(u'', lcid=0x7C14)
    ]


class Swaziland(Locale):
    _iso_code = 'SZ'
    english_name = 'Swaziland'
    _flag = 'flags\\SZ.png'
    languages = [
        English(u'Swaziland', lcid=0x1000),
        Swati(u'káNgwane', lcid=None)
    ]


class Sweden(Locale):
    _iso_code = 'SE'
    english_name = 'Sweden'
    _flag = 'flags\\SE.png'
    languages = [
        Swedish(u'Sverige', lcid=0x041D),
        English(u'Sweden', lcid=0x0009),
        SamiLule(u'', lcid=0x7C3B),
        SamiNorthern(u'', lcid=0x003B),
        SamiSouthern(u'', lcid=0x783B)
    ]


class Switzerland(Locale):
    _iso_code = 'CH'
    english_name = 'Switzerland'
    _flag = 'flags\\CH.png'
    languages = [
        German(u'Schweiz', lcid=0x0807),
        French(u'Suisse', lcid=0x100C),
        Italian(u'Svizzera', lcid=0x0810),
        Romansh(u'Svizra', lcid=0x0417),
        SwissGerman(u'', lcid=0x0084),
        English(u'Switzerland', lcid=0x0009),
        Portuguese(u'', lcid=0x0016),
        Walser(u'', lcid=0x1000)
    ]


class Syria(Locale):
    _iso_code = 'SY'
    english_name = 'Syria'
    _flag = 'flags\\SY.png'
    languages = [
        Arabic(u'سورية', lcid=0x2801),
        Kurdish(u'Sūriyya', lcid=None),
        French(u'', lcid=0x000C),
        Syriac(u'', lcid=0x005A)
    ]


class Taiwan(Locale):
    _iso_code = 'TW'
    english_name = 'Taiwan'
    _flag = 'flags\\TW.png'
    languages = [
        ChineseTraditional(u'中華民國', lcid=0x0404)
    ]


class Tajikistan(Locale):
    _iso_code = 'TJ'
    english_name = 'Tajikistan'
    _flag = 'flags\\TJ.png'
    languages = [
        Russian(u'Таджикистан', lcid=None),
        TajikCyrillic(u'Тоҷикистон', lcid=0x0428)
    ]


class Tanzania(Locale):
    _iso_code = 'TZ'
    english_name = 'Tanzania'
    _flag = 'flags\\TZ.png'
    languages = [
        English(u'Tanzania', lcid=0x1000),
        Swahili(u'Tanzania', lcid=0x1000),
        Asu(u'', lcid=0x1000),
        Bena(u'', lcid=0x1000),
        Langi(u'', lcid=0x1000),
        Machame(u'', lcid=0x1000),
        Makonde(u'', lcid=0x1000),
        Masai(u'', lcid=0x1000),
        Rombo(u'', lcid=0x1000),
        Rwa(u'', lcid=0x1000),
        Sangu(u'', lcid=0x1000),
        Shambala(u'', lcid=0x1000),
        Vunjo(u'', lcid=0x1000)
    ]


class Thailand(Locale):
    _iso_code = 'TH'
    english_name = 'Thailand'
    _flag = 'flags\\TH.png'
    languages = [
        Thai(u'เมืองไทย', lcid=0x041E)
    ]


class TheGambia(Locale):
    _iso_code = 'GM'
    english_name = 'The Gambia'
    _flag = 'flags\\GM.png'
    languages = [
        English(u'The Gambia', lcid=0x1000)
    ]


class TheNetherlands(Locale):
    _iso_code = 'NL'
    english_name = 'The Netherlands'
    _flag = 'flags\\NL.png'
    languages = [
        Dutch(u'Nederland', lcid=0x0413),
        English(u'The Netherlands', lcid=0x0009),
        Frisian(u'', lcid=0x0062),
        LowGerman(u'', lcid=0x1000)
    ]


class Tifinagh(Locale):
    _iso_code = 'Tfng'
    english_name = 'Tifinagh'
    _flag = None
    languages = [
        StandardMoroccanTamazight(u'', lcid=0x1000),
        Tachelhit(u'', lcid=0x1000)
    ]


class TimorLeste(Locale):
    _iso_code = 'TL'
    english_name = 'Timor-Leste'
    _flag = 'flags\\TL.png'
    languages = [
        Portuguese(u'Timor-Leste', lcid=0x1000),
        Tetum(u'Timor Lorosa\'e', lcid=None)
    ]


class Togo(Locale):
    _iso_code = 'TG'
    english_name = 'Togo'
    _flag = 'flags\\TG.png'
    languages = [
        French(u'Togo', lcid=0x1000),
        Ewe(u'Togo', lcid=0x1000)
    ]


class Tokelau(Locale):
    _iso_code = 'TK'
    english_name = 'Tokelau'
    _flag = 'flags\\TK.png'
    languages = [
        English(u'Tokelau', lcid=0x1000),
        Samoan(u'Tokelau', lcid=None),
        Tokelauan(u'Tokelau', lcid=None)
    ]


class Tonga(Locale):
    _iso_code = 'TO'
    english_name = 'Tonga'
    _flag = 'flags\\TO.png'
    languages = [
        English(u'Tonga', lcid=0x1000),
        Tongan(u'Tonga', lcid=0x1000)
    ]


class TrinidadandTobago(Locale):
    _iso_code = 'TT'
    english_name = 'Trinidad and Tobago'
    _flag = 'flags\\TT.png'
    languages = [
        English(u'Trinidad and Tobago', lcid=0x2C09)
    ]


class Tunisia(Locale):
    _iso_code = 'TN'
    english_name = 'Tunisia'
    _flag = 'flags\\TN.png'
    languages = [
        Arabic(u'تونس', lcid=0x1C01),
        French(u'Tunisie', lcid=0x1000)
    ]


class Turkey(Locale):
    _iso_code = 'TR'
    english_name = 'Turkey'
    _flag = 'flags\\TR.png'
    languages = [
        Turkish(u'Türkiye', lcid=0x041F)
    ]


class Turkmenistan(Locale):
    _iso_code = 'TM'
    english_name = 'Turkmenistan'
    _flag = 'flags\\TM.png'
    languages = [
        Turkmen(u'Türkmenistan', lcid=0x0442)
    ]


class TurksandCaicosIslands(Locale):
    _iso_code = 'TC'
    english_name = 'Turks and Caicos Islands'
    _flag = 'flags\\TC.png'
    languages = [
        English(u'Turks and Caicos Islands', lcid=0x1000)
    ]


class Tuvalu(Locale):
    _iso_code = 'TV'
    english_name = 'Tuvalu'
    _flag = 'flags\\TV.png'
    languages = [
        English(u'Tuvalu', lcid=0x1000)
    ]


class Uganda(Locale):
    _iso_code = 'UG'
    english_name = 'Uganda'
    _flag = 'flags\\UG.png'
    languages = [
        English(u'Uganda', lcid=0x1000),
        Swahili(u'Uganda', lcid=0x1000),
        Chiga(u'', lcid=0x1000),
        Ganda(u'', lcid=0x1000),
        Nyankole(u'', lcid=0x1000),
        Soga(u'', lcid=0x1000),
        Teso(u'', lcid=0x1000)
    ]


class Ukraine(Locale):
    _iso_code = 'UA'
    english_name = 'Ukraine'
    _flag = 'flags\\UA.png'
    languages = [
        Ukrainian(u'Україна', lcid=0x0422),
        Russian(u'', lcid=0x0019)
    ]


class UnitedArabEmirates(Locale):
    _iso_code = 'AE'
    english_name = 'United Arab Emirates'
    _flag = 'flags\\AE.png'
    languages = [
        Arabic(u'الإمارات العربيّة المتّحدة', lcid=0x3801),
        Azerbaijani(u'Birləşmiş Ərəb Əmirlikləri', lcid=None)
    ]


class UnitedKingdom(Locale):
    _iso_code = 'GB'
    english_name = 'United Kingdom'
    _flag = 'flags\\GB.png'
    languages = [
        Welsh(u'Y Deyrnas Unedig', lcid=0x0452),
        English(u'United Kingdom', lcid=0x0809),
        Irish(u'Ríocht Aontaithe', lcid=None),
        ScottishGaelic(u'Rìoghachd Aonaichte', lcid=0x0491),
        Cornish(u'An Rywvaneth Unys', lcid=0x1000)
    ]


class UnitedStatesMinorOutlyingIslands(Locale):
    _iso_code = 'UM'
    english_name = 'United States Minor Outlying Islands'
    _flag = 'flags\\UM.png'
    languages = [
        English(u'United States Minor Outlying Islands', lcid=0x1000)
    ]


class UnitedStatesVirginIslands(Locale):
    _iso_code = 'VI'
    english_name = 'United States Virgin Islands'
    _flag = 'flags\\VI.png'
    languages = [
        English(u'United States Virgin Islands', lcid=0x1000)
    ]


class UnitedStatesofAmerica(Locale):
    _iso_code = 'US'
    english_name = 'United States of America'
    _flag = 'flags\\US.png'
    languages = [
        English(u'United States of America', lcid=0x0409),
        Cherokee(u'', lcid=0x045C),
        Hawaiian(u'‘Amelika Hui Pū ‘la', lcid=0x0075),
        Lakota(u'', lcid=0x1000),
        Spanish(u'Estados Unidos', lcid=0x000A)
    ]


class Uruguay(Locale):
    _iso_code = 'UY'
    english_name = 'Uruguay'
    _flag = 'flags\\UY.png'
    languages = [
        Spanish(u'Uruguay', lcid=0x380A)
    ]


class Uzbekistan(Locale):
    _iso_code = 'UZ'
    english_name = 'Uzbekistan'
    _flag = 'flags\\UZ.png'
    languages = [
        KaraKalpak(u'O\'zbekstan', lcid=None),
        UzbekLatin(u'O\'zbekiston', lcid=0x0443),
        UzbekCyrillic(u'Ўзбекистон', lcid=0x0843)
    ]


class Vanuatu(Locale):
    _iso_code = 'VU'
    english_name = 'Vanuatu'
    _flag = 'flags\\VU.png'
    languages = [
        Bislama(u'Vanuatu', lcid=None),
        English(u'Vanuatu', lcid=0x1000),
        French(u'Vanuatu', lcid=0x1000)
    ]


class Venezuela(Locale):
    _iso_code = 'VE'
    english_name = 'Venezuela'
    _flag = 'flags\\VE.png'
    languages = [
        Spanish(u'Venezuela', lcid=0x200A)
    ]


class Vietnam(Locale):
    _iso_code = 'VN'
    english_name = 'Vietnam'
    _flag = 'flags\\VN.png'
    languages = [
        Vietnamese(u'Việt Nam', lcid=0x042A)
    ]


class WallisandFutuna(Locale):
    _iso_code = 'WF'
    english_name = 'Wallis and Futuna'
    _flag = 'flags\\WF.png'
    languages = [
        French(u'Wallis-et-Futuna', lcid=0x1000)
    ]


class WesternSahara(Locale):
    _iso_code = 'EH'
    english_name = 'Western Sahara'
    _flag = 'flags\\EH.png'
    languages = [
        Arabic(u'الصحراء الغربية', lcid=None),
        Spanish(u'Sahara Occidental', lcid=None),
        French(u'Sahara occidental', lcid=None)
    ]


class World(Locale):
    _iso_code = '001'
    english_name = 'World'
    _flag = None
    languages = [
        Arabic(u'', lcid=0x0001),
        English(u'World', lcid=0x0009),
        Esperanto(u'', lcid=0x1000),
        Interlingua(u'', lcid=0x1000),
        Volapuk(u'', lcid=0x1000)
    ]


class Yemen(Locale):
    _iso_code = 'YE'
    english_name = 'Yemen'
    _flag = 'flags\\YE.png'
    languages = [
        Arabic(u'اليمن', lcid=0x2401)
    ]


class Zambia(Locale):
    _iso_code = 'ZM'
    english_name = 'Zambia'
    _flag = 'flags\\ZM.png'
    languages = [
        English(u'Zambia', lcid=0x1000),
        Bemba(u'Zambia', lcid=0x1000)
    ]


class Zimbabwe(Locale):
    _iso_code = 'ZW'
    english_name = 'Zimbabwe'
    _flag = 'flags\\ZW.png'
    languages = [
        English(u'Zimbabwe', lcid=0x3009),
        NorthNdebele(u'Zimbabwe', lcid=0x1000),
        Shona(u'Zimbabwe', lcid=0x1000)
    ]


if __name__ == '__main__':
    pass
    # found_wx_codes = []
    # found_lcid_codes = []
    #
    # for c in countries:
    #     print(c.english_name)
    #     print('    COUNTRY CODE:', c.code)
    #     for l in c.languages:
    #         l_lcid = l.lcid
    #         w_code = l.wx_code
    #         print('   ', l.english_name)
    #         print('   ', l.country_name)
    #         print('        LANGUAGE CODES:', l.locale_names)
    #         print('        LCID:          ', l_lcid)
    #         print('        WX CODE:       ', w_code)
    #
    #         if l_lcid is not None and l_lcid not in found_lcid_codes:
    #             found_lcid_codes += [l_lcid]
    #
    #         if w_code is not None and w_code not in found_wx_codes:
    #             found_wx_codes += [w_code]
    # print('\n')
    # print('FOUND LCID COUNT:', len(found_lcid_codes))
    # print('FOUND WX COUNT:  ', len(found_wx_codes))
    # print('WX CODE COUNT:   ', len(list(LCID_TO_WX.keys())))
    #
    # import sys
    #
    # mod = sys.modules[__name__]
    # num_countries = 0
    # num_languages = 0
    # num_country_languages = 0
    #
    # for cls_val in mod.__dict__.values():
    #     try:
    #         if issubclass(cls_val, Country):
    #             num_countries += 1
    #             num_country_languages += len(cls_val.languages)
    #         elif issubclass(cls_val, Language):
    #             num_languages += 1
    #     except TypeError:
    #         pass
    #
    # print('NUMBER OF COUNTRIES:         ', num_countries)
    # print('NUMBER OF LANGUAGES:         ', num_languages)
    # print('NUMBER OF COUNTRY LANGUAGES: ', num_country_languages)
