import json, requests, lzma, gzip, bz2
import time
def search_json(link):
    with open('app/db/link_count.json', 'r+') as json_file:
        data = json.load(json_file)
        if data.get(link) == None:
            data.update({link: 1})
        else:
            count = data[link]
            data[link] = count + 1
        json_file.seek(0)
        json_file.truncate()
        json.dump(data, json_file, indent=4)
        json_file.close()

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
    if link.endswith('/') == True:
        ptlink = link + 'Packages'
        bzlink = link + 'Packages.bz2'
    else:
        ptlink = link + '/Packages'
        bzlink = link + '/Packages.bz2'
    rn = time.time()
    try:
        now = time.time()
        print('Started to Hit Repo for .bz2 at %s' % (now - rn))
        packages = res.get(bzlink, headers=headers).content
        packages_dec = bz2.decompress(packages)
        return packages_dec
    except:
        try:
            now = time.time()
            print('Started to Hit Repo for plaintext at %s' % (now - rn))
            packages = res.get(ptlink, headers=headers).content
            return packages
        except:
            return None

def packages_to_json(link, packages):
    list_of_entries = packages.decode('utf-8').splitlines()
    package_json = {}
    package_ids = []
    filenames = []
    names = []
    authors = []
    versions = []
    descriptions = []
    icons = []
    for entry in list_of_entries:
        key = entry.split(":", 1)
        if key[0] == 'Filename':
            filenames.append(key[1])
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
    package_json = []
    for i in range(len(package_ids)):
        package_json.append({
            package_ids[i]: {
                'name': names[i],
                'author': authors[i],
                'download_link': link + filenames[i],
                'version': versions[i],
                'description': descriptions[i]
            }
        })
    return package_json
