import json, requests, lzma, gzip, bz2
import time
import traceback
from flask import make_response, render_template

def get_packages(link):
    res = requests.session()
    headers = {
        'User-Agent': 'Sileo/1 CFNetwork/976 Darwin/18.2.0',
        'X-Firmware': '12.1.2',
        'X-Machine': 'iPhone10,3',
        'X-Unique-ID': 'df2b5bc80c02907c03dc65e9f38eedfa350711bb',
        'Authority': link,
        'Accept': '*/*',
        'Keep-Alive': 'True'
    }
    ptlink = link + '/Packages'
    bzlink = link + '/Packages.bz2'
    try:
        packages = res.get(bzlink, headers=headers).content
        packages_dec = bz2.decompress(packages)
        res.close()
        return packages_dec
    except:
        try:
            packages = res.get(ptlink, headers=headers).content
            res.close()
            return packages
        except:
            res.close()
            return None

def packages_to_json(link, packages):
    try:
        list_of_entries = packages.decode('utf-8').splitlines()
        package_json = {}
        package_ids = []
        filenames = []
        names = []
        authors = []
        versions = []
        descriptions = []
        icons = []
        depictions = []
        sileodepictions = []
        maintainers = []
        dependencies = []
        conflicts = []
        packages = []
        for entry in list_of_entries:
            key = entry.split(":", 1)
            if key[0] == 'Filename':
                filenames.append(key[1])
            elif key[0] == 'Depiction':
                depictions.append(key[1])
            elif key[0].lower() == 'sileodepiction':
                sileodepictions.append(key[1])
            elif key[0] == 'Maintainer':
                maintainers.append(key[1])
            elif key[0] == 'Name':
                names.append(key[1])
            elif key[0] == 'Package':
                package_ids.append(key[1])
            elif key[0] == 'Icon':
                icons.append(key[1])
            elif key[0] == 'Version':
                versions.append(key[1])
            elif key[0] == 'Description':
                descriptions.append(key[1])
            elif key[0] == 'Author':
                authors.append(key[1])
            elif key[0] == 'Depends':
                dependencies.append(key[1])
            elif key[0] == 'Conflicts':
                conflicts.append(key[1])
        package_json = []
        count = 0
        print(package_ids)
        for i in range(len(package_ids)):
            try:
                filename = filenames[i][1:]
            except:
                filename = ""
            try:
                name = names[i][1:]
            except:
                name = ""
            try:
                author = authors[i][1:]
            except:
                author = ''
            try:
                version = versions[i][1:]
            except:
                version = ''
            try:
                description = descriptions[i][1:]
            except:
                description = ''
            try:
                maintainer = maintainers[i][1:]
            except:
                maintainer = ''
            try:
                depiction = depictions[i][1:]
            except:
                depiction = ""
            try:
                conflict = conflicts[i][1:]
            except:
                conflict = 'No Conflicts'
            try:
                dependency = dependencies[i][1:]
            except:
                dependency = 'No Dependenies'
            try:
                package = package_ids[i][1:]
            except:
                package = 'Unknown Package ID'
            package_json.append({
                    'name': name,
                    'author': author,
                    'download_link': link + '/' + filename,
                    'version': version,
                    'description': description,
                    'maintainer': maintainer,
                    'depiction': depiction,
                    'dependencies': dependency,
                    'conflicts': conflict,
                    'package': package
                })
            count += 1
        return package_json
    except:
        print(traceback.format_exc())