from scapy.layers.x509 import *
from scapy.asn1.asn1 import *
from scapy.utils import *
from scapy.layers.x509 import RSAPrivateKey

# Serialize key
a = RSAPrivateKey()
print(a.show())
k = a.self_build()
b = RSAPrivateKey(a)
print(b.show())



# Deserialize key
k = base64_bytes('MIIEowIBAAKCAQEAmFdqP+nTEZukS0lLP+yj1gNImsEIf7P2ySTunceYxwkm4VE5QReDbb2L5/HL\nA9pPmIeQLSq'
                 '/BgO1meOcbOSJ2YVHQ28MQ56+8Crb6n28iycX4hp0H3AxRAjh0edX+q3yilvYJ4W9\n/NnIb/wAZwS0oJif/tTkVF77HybAfJde5Eqbp+bCKIvMWnambh9DRUyjrBBZo5dA1o32zpuFBrJd\nI8dmUpw9gtf0F0Ba8lGZm8Uqc0GyXeXOJUE2u7CiMu3M77BM6ZLLTcow5+bQImkmTL1SGhzwfinM\nE1e6p3Hm//pDjuJvFaY22k05LgLuyqc59vFiB3Toldz8+AbMNjvzAwIDAQABAoIBAH3KeJZL2hhI\n/1GXNMaU/PfDgFkgmYbxMA8JKusnm/SFjxAwBGnGI6UjBXpBgpQs2Nqm3ZseF9u8hmCKvGiCEX2G\nesCo2mSfmSQxD6RBrMTuQ99UXpxzBIscFnM/Zrs8lPBARGzmF2nI3qPxXtex4ABX5o0Cd4NfZlZj\npj96skUoO8+bd3I4OPUFYFFFuv81LoSQ6Hew0a8xtJXtKkDp9h1jTGGUOc189WACNoBLH0MGeVoS\nUfc1++RcC3cypUZ8fNP1OO6GBfv06f5oXES4ZbxGYpa+nCfNwb6V2gWbkvaYm7aFn0KWGNZXS1P3\nOcWv6IWdOmg2CI7MMBLJ0LyWVCECgYEAyMJYw195mvHl8VyxJ3HkxeQaaozWL4qhNQ0Kaw+mzD+j\nYdkbHb3aBYghsgEDZjnyOVblC7I+4smvAZJLWJaf6sZ5HAw3zmj1ibCkXx7deoRc/QVcOikl3dE/\nymO0KGJNiGzJZmxbRS3hTokmVPuxSWW4p5oSiMupFHKa18Uv8DECgYEAwkJ7iTOUL6b4e3lQuHQn\nJbsiQpd+P/bsIPP7kaaHObewfHpfOOtIdtN4asxVFf/PgW5uWmBllqAHZYR14DEYIdL+hdLrdvk5\nnYQ3YfhOnp+haHUPCdEiXrRZuGXjmMA4V0hL3HPF5ZM8H80fLnN8Pgn2rIC7CZQ46y4PnoV1nXMC\ngYBBwCUCF8rkDEWa/ximKo8aoNJmAypC98xEa7j1x3KBgnYoHcrbusok9ajTe7F5UZEbZnItmnsu\nG4/Nm/RBV1OYuNgBb573YzjHl6q93IX9EkzCMXc7NS7JrzaNOopOj6OFAtwTR3m89oHMDu8W9jfi\nKgaIHdXkJ4+AuugrstE4gQKBgFK0d1/8g7SeA+Cdz84YNaqMt5NeaDPXbsTA23QxUBU0rYDxoKTd\nFybv9a6SfA83sCLM31K/A8FTNJL2CDGA9WNBL3fOSs2GYg88AVBGpUJHeDK+0748OcPUSPaG+pVI\nETSn5RRgffq16r0nWYUvSdAn8cuTqw3y+yC1pZS6AU8dAoGBAL5QCi0dTWKN3kf3cXaCAnYiWe4Q\ng2S+SgLE+F1U4Xws2rqAuSvIiuT5i5+Mqk9ZCGdoReVbAovJFoRqe7Fj9yWM+b1awGjL0bOTtnqx\n0iljob6uFyhpl1xgW3a3ICJ/ZYLvkgb4IBEteOwWpp37fX57vzhW8EmUV2UX7ve1uNRI')
x = RSAPrivateKey(k)
print(x.show())


# = Key class : key modulus
# x.modulus == ASN1_INTEGER(19231328316532061413420367242571475005688288081144416166988378525696075445024135424022026378563116068168327239354659928492979285632474448448624869172454076124150405352043642781483254546569202103296262513098482624188672299255268092629150366527784294463900039290024710152521604731213565912934889752122898104556895316819303096201441834849255370122572613047779766933573375974464479123135292080801384304131606933504677232323037116557327478512106367095125103346134248056463878553619525193565824925835325216545121044922690971718737998420984924512388011040969150550056783451476150234324593710633552558175109683813482739004163)
#
# = Key class : key public exponent
# x.publicExponent == ASN1_INTEGER(65537)
#
# = Key class : key private exponent
# x.privateExponent == ASN1_INTEGER(15879630313397508329451198152673380989865598204237760057319927734227125481903063742175442230739018051313441697936698689753842471306305671266572085925009572141819112648211571007521954312641597446020984266846581125287547514750428503480880603089110687015181510081018160579576523796170439894692640171752302225125980423560965987469457505107324833137678663960560798216976668670722016960863268272661588745006387723814962668678285659376534048525020951633874488845649968990679414325096323920666486328886913648207836459784281744709948801682209478580185160477801656666089536527545026197569990716720623647770979759861119273292833)
#
# = Key class : key prime1
# x.prime1 == ASN1_INTEGER(140977881300857803928857666115326329496639762170623218602431133528876162476487960230341078724702018316260690172014674492782486113504117653531825010840338251572887403113276393351318549036549656895326851872473595350667293402676143426484331639796163189182788306480699144107905869179435145810212051656274284113969)
#
# = Key class : key prime2
# x.prime2 == ASN1_INTEGER(136413798668820291889092636919077529673097927884427227010121877374504825870002258140616512268521246045642663981036167305976907058413796938050224182519965099316625879807962173794483933183111515251808827349718943344770056106787713032506379905031673992574818291891535689493330517205396872699985860522390496583027)
#
# = Key class : key exponent1
# x.exponent1 == ASN1_INTEGER(46171616708754015342920807261537213121074749458020000367465429453038710215532257783908950878847126373502288079285334594398328912526548076894076506899568491565992572446455658740752572386903609191774044411412991906964352741123956581870694330173563737928488765282233340389888026245745090096745219902501964298369)
#
# = Key class : key exponent2
# x.exponent2 == ASN1_INTEGER(58077388505079936284685944662039782610415160654764308528562806086690474868010482729442634318267235411531220690585030443434512729356878742778542733733189895801341155353491318998637269079682889033003797865508917973141494201620317820971253064836562060222814287812344611566640341960495346782352037479526674026269)
#
# = Key class : key coefficient
# x.coefficient == ASN1_INTEGER(133642091354977099805228515340626956943759840737228695249787077343495440064451558090846230978708992851702164116059746794777336918772240719297253693109788134358485382183551757562334253896010728509892421673776502933574360356472723011839127418477652997263867089539752161307227878233961465798519818890416647361608)
