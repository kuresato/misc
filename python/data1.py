# -*- coding: utf-8 -*-
import sys
def cat(fname):
    try:
        file = open(fname,"r")
        for line in file:
            # 改行せずに出力
            sys.stdout.write(line)
        file.close()
    except IOError as e:
        print "IOError: {0}".format(e)
    except:
        print "Unexpected error:", sys.exc_inf()[0]
        raise

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "ファイル名を指定してください"
    else:
        cat(sys.argv[1])


