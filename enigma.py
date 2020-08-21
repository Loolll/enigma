import sys
import argparse
import __bmpIn__ as bmpIn
import __bmpOut__ as bmpOut
import __keyword__ as key


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt', default=False)
    parser.add_argument('-d', '--decrypt', default=False)
    parser.add_argument('-c', '--code', default=False)
    parser.add_argument('-p', '--password', default='0')
    parser.add_argument('-f', '--result_file', default=False)
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if (namespace.encrypt):
        if (namespace.result_file):
            bmpIn.mainI(namespace.encrypt, namespace.password, namespace.result_file)
        else:
            bmpIn.mainI(namespace.encrypt, namespace.password, "result.bmp")
    elif (namespace.decrypt):
        if (namespace.result_file):
            bmpOut.mainI(namespace.decrypt, namespace.password, namespace.result_file)
        else:
            bmpOut.mainI(namespace.decrypt, namespace.password, "result.txt")
    elif (namespace.code):
        if (namespace.result_file):
            key.mainI(namespace.code, namespace.result_file)
        else:
            key.mainI(namespace.code, "key.bmp")
    else:
        print("Run with -h to see help")
