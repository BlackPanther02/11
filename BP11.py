# Encrypt by Botol Baba
# Github : https://github.com/BlackPanther
# Facebook : https://facebook.com/Mahbub.Alam.Khan.02
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
