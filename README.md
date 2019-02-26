# pyWinLocale

Windows Locale Simplified

This is a pretty straight forward language/locale implementation.
It removes most of the complexities when dealing with th setting of a
Microsoft Windows locale in python and wxPython

wxPython is optional
<br></br>
<br></br>
***Basic use examples***
________________________
```python
import pyWinLocale
```

the above will always be assumed

the structure is broken down by locale and each locale contains the
languages that are supported for the current version of Windows that is
running, this includes any language packs that may be installed.

to access the supported locales there are the 3 ways listed below.

```python
for locale in pyWinLocale.locales:
    print(locale.english_name, locale.code)
```

you can also directly access a locale by it's 2 letter country code

```python
locale = pyWinLocale.locales['US']
```

or if you want as an attribute
```python
locale = pyWinLocale.locales.US
```

you can also get a locale by the Windows LCID by accessing the
locales object as if it was a list with the index set to the LCID
I am using thee LCID 0x1000 to show. Do not use the 0x1000 LCID, if the
locale has that LCID then you will have to locate the locale by it's 2
letter country code. the LCID 0x100 means that Windows does not have an
LCID set for that locale. (there are a bunch of them that use 0x1000)

```python
locale = pyWinLocale.locales[0x1000]
```

getting a language that is supported by a locale (country) works in
the same manner as getting the locale. The only difernce is you will
want to perform the operations on the locale object instead.

```python
for locale in pyWinLocale.locales:
    for language in locale:

```

you can also directly access a locale by it's 2 letter country code

```python
locale = pyWinLocale.locales['US']
language = locale['en']
```

or if you want as an attribute
```python
locale = pyWinLocale.locales.US
language = locale.en
```


pretty simple that way. using the `pyWinLocale.locales` objct is only
going to return languages and locals that are supported.
if you have a need to access the locales and languages for those locales
you can do this by accessing the class for the specific locale directly.


```python
germany = pyWinLocale.Germany()
for lannguage in germany:
    print languag.iso_code
```

this is going to give you all available languages and any locale you want
even if the version of Windows the program is running on does not support it.
<br></br>
<br></br>
***Windows default user locale/language***
__________________________________________
If you want to get the current user defined language that is set in
Windows.

```python
language = pyWinLocale.get_windows_user_language()
```

by default if a languagee cannot be found that matches the user defined
language. the languag 'en-US' will be returned. You can change this
by setting `pyWinLocale.DEFAULT_USER_LANGUAGE` to the string locale
you want to use as a default before calling
`pyWinLocale.get_windows_user_language`
<br></br>
<br></br>
***Native names***
__________________
Here are a few bonuses.

I have also included the country name and the language name in
native script. It is always nic to provide a language selection dialog
that lists the countries and languages in the language they are for.

```python
language = pyWinLocale.get_windows_user_language()
print(language.locale_name)
print(language.native_name)
```
<br></br>
<br></br>
***Flag icons***
________________
I have also included flag icons for all but 5 of the locals available.
the returned values are byte strings.
```python
language = pyWinLocale.get_windows_user_language()
print(language.locale.flag)
```
<br></br>
<br></br>
***Setting the Python locale***
_______________________________
You can also set the locale in python via the language as well.
Windows starting with Windows 10 build 1809 will cause Python to throw
an error if the user defined locale is a locale that does not have a
unique LCID assigned to it. and in Windows 10 there are alot of them.
these aree locales that have an LCID of 0x1000. If you set the locale
by using the `set_locale` method in a language it bypasses this issue.

```python
language = pyWinLocale.get_windows_user_language()
language.set_local()
```
<br></br>
<br></br>
***wxPython***
______________
For the folks that use wxPython. you may already know about the issues
with `wx.Locale.GetSystemLanguage` well it does exactly that it gets the
system language and not the user language. wxPython does not have the
ability to collect the user defined language. and because `wx.LANGUAGE_\*`
constants do not map directly to LCID's this becomes a real headache.

Well the headache is now GONE. I have taken care of the ugly for ya.
calling the `set_wx_local` method is going to get the currently running
`wx.App` instance and load the locale, thene it is going to store that
locale to the app instance as the attribute `locale`

```python
language = pyWinLocale.get_windows_user_language()
language.set_wx_local()
```

<br></br>
***pyWinLocal.Language attributes***
____________________________________
* `ISO639_1` : 2 letter language code or `None`
* `ISO639_2` : 3 letter language code or `None`
* `ISO639_3` : all others or `None`
* `english_name` : english name for the language
* `native_name` : language name in native script

<br></br>
***pyWinLocal.Language instance variables***
____________________________________________
* `locale_name` : the name of the locale (country) in native script
* `locale` : the parent locale (country)

<br></br>
***pyWinLocal.Language properties***
____________________________________
* `label` : the same thing as the instance variable `locale_name`
* `iso_code` : because of the nature of Windows there are varying iso codes
for the same language locale combination (varying dialects and such) this
property will return the one that represents this locale/language pairing
that Windows uses.
* `lang_iso_code` : This is the language portion of the iso code.
The locale portion is always the last 2 characters after the last'-'
this returns everything before that
* `wx_code` : The `wx.LANGUAGE_*` code that matches the locale/language or `None`

<br></br>
***pyWinLocal.Language methods***
_________________________________
* `set_locale` : explained above
* `set_wx_locale` : explained above

<br></br>
***pyWinLocal.Locale attributes***
__________________________________
* `english_name` : english name of the locale (country)
* `languages` : list of the languages available for the locale (country)

<br></br>
***pyWinLocal.Locale properties***
__________________________________
* `locale_iso_code` : 2 letter locale string
* `flag` : byte string for the flag icon or `None`
