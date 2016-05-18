import os
import urllib
import tarfile

URL = ("http://www.cs.cornell.edu/people/pabo/"
       "movie-review-data/review_polarity.tar.gz")

ARCHIVE_NAME = URL.rsplit('/', 1)[1]
DATA_FOLDER = "txt_sentoken"


if not os.path.exists(DATA_FOLDER):

    if not os.path.exists(ARCHIVE_NAME):
        print "Downloading dataset from %s (3 MB)" % URL
        opener = urllib.urlopen(URL)
        open(ARCHIVE_NAME, 'wb').write(opener.read())

    print "Decompressing %s" % ARCHIVE_NAME
    tarfile.open(ARCHIVE_NAME, "r:gz").extractall(path='.')
    os.remove(ARCHIVE_NAME)