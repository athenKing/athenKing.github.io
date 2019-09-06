prefix='https://raw.githubusercontent.com/nailperry-zd/The-Economist/master/'

url="${prefix}$1-$2-$3/TE_$1$2$3.pdf"

proxy wget "${url}"