#!/usr/bin/env python

from os import path
import subprocess
from glob import glob
import re
import sys


def run(x) -> str:
    print(x)
    p: subprocess.CompletedProcess = subprocess.run(x, capture_output=True, shell=True)
    assert p.returncode == 0
    return p.stdout.decode('utf-8')


def rst_to_md():
    s2editortuts = "/mnt/nt1/sc2mapster/s2editor-tutorials-master"

    for srcName in glob('%s/**/*.rst' % (s2editortuts)):
        docPath = path.splitext(path.relpath(srcName, s2editortuts))[0]

        # exclude manually edited
        excludeDocs = ['001_Editor_Introduction', '002_Getting_to_the_Editor', '003_Navigating_the_Interface']
        if path.basename(docPath) in excludeDocs:
            continue

        targetName = 'docs/New_Tutorials/%s.md' % docPath
        run('pandoc -f rst --wrap=none -t gfm+smart -o %s %s' % (targetName, srcName))
        with open(targetName, mode="r+") as f:
            content = f.read()

            # change '# TITLE CASE' to '# Title Case'
            def replHeadTitle(m: re.Match):
                return '%s %s' % (m.group(1), m.group(2).title())
            content = re.sub(r'^(#+)\s+(.+)$', replHeadTitle, content, flags=re.M)

            # respect new location of images
            def replImageResource(m: re.Match):
                numPattern = '%02d' if srcName.find('01_Introduction') != -1 else '%01d'
                imgName = re.sub(r'/image([\d]+)', lambda x : numPattern % int(x[1]), m.group(2))
                imgPath = './resources/' + imgName
                return m.group(1) + ('(%s)' % imgPath)
            content = re.sub(r'(\!\[Image\d*\])\(\./([^\)]+)\)', replImageResource, content, flags=re.M | re.I)

            # add alt attribute properly for images.. and a caption if seems appropiate
            def replImageAlt(m: re.Match):
                alt = m.group(2)
                if len(alt) > 40:
                    alt = ""
                return '![%s](%s)\n*%s*\n' % (alt, m.group(1), m.group(2))
            content = re.sub(r'^\.?\!\[Image\d*\]\(([^\)]+)\)\n\n([ -~]{1,70})\n', replImageAlt, content, flags=re.M | re.I)

            # add links for images larger than document width
            def replImageLinks(m: re.Match):
                imgPath = m.group(2)
                width = run('identify -format "%%w" %s' % path.join(path.dirname(targetName), imgPath))
                o = m.group(0)
                if int(width) > 600:
                    o = '[%s](%s)' % (o, imgPath)
                return o
            content = re.sub(r'(\!\[[ -~]+\])\(([^\)]+)\)', replImageLinks, content, flags=re.M | re.I)

            f.seek(0)
            f.truncate()
            f.write(content)


def add_map_links():
    docAttachments = {}

    for srcMap in glob('**/*.SC2Map', recursive=True):
        docId = re.match(r'([\d]+)', path.basename(srcMap))[1]
        if docId not in docAttachments:
            docAttachments[docId] = []
        docAttachments[docId].append(srcMap)

    for docId in docAttachments:
        # these don't have a matching documentation
        if docId in ['069', '090', '080']:
            continue

        srcDoc = run('fd -e md %s' % docId).split()
        assert len(srcDoc) == 1
        srcDoc: str = srcDoc[0]

        with open(srcDoc, mode="a+") as f:
            f.write('\n## Attachments\n\n')
            for srcMap in docAttachments[docId]:
                mapName = path.basename(srcMap)
                f.write(' * [%s](%s)\n' % (mapName, './maps/' + mapName))


if __name__ == '__main__':
    locals()[sys.argv[1]]()
