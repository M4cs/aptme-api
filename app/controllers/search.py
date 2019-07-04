import json, requests, lzma, gzip, bz2
import time, os
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
        
def cache_packages(link, template):
    with open('app/db/{}.html'.format(link.replace('/', '-')), 'w') as html:
        html.write(template)
    return True

def check_cache(link):
    return os.path.exists('app/db/{}.html'.format(link.replace('/', '-')))

def grab_cache(link):
    with open('app/db/{}.html'.format(link.replace('/', '-')), 'r') as html:
        template = html.read()
    return str(template)

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
        return packages_dec
    except:
        try:
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
    dependencies = []
    conflicts = []
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
        elif key[0] == 'Depends':
            dependencies.append(key[1])
        elif key[0] == 'Conflicts':
            conflicts.append(key[1])
    package_json = []
    count = 0
    for i in range(len(package_ids)):
        try:
            try:
                filename = filenames[i][1:]
            except:
                filename = ''
            try:
                name = names[i][1:]
            except:
                name = package_ids[i]
            try:
                author = authors[i][1:]
            except:
                author = 'Unknown'
            try:
                version = versions[i][1:]
            except:
                version = 'Unknown'
            try:
                description = descriptions[i][1:]
            except:
                description = 'No Description'
            try:
                conflict = conflicts[i][1:]
            except:
                conflict = 'No Conflicts'
            try:
                dependency = dependencies[i][1:]
            except:
                dependency = 'No Dependenies'
            package_json.append([{
                    'name': name,
                    'author': author,
                    'download_link': link + '/' + filename,
                    'version': version,
                    'description': description,
                    'conflicts': conflict,
                    'dependencies': dependency
                }])
            count += 1
        except:
            print('FAILED')
            pass
    print(package_json)
    return package_json

def generate_template(list_of):
    template = """\
      <div class="card" style="margin: 5px;">
        <div class="card-body">
            <span style="float:right">
              <a class="btn btn-primary btn-round" alt="Download" title="Download" href="{download_link}"><i class="fa fa-download" style="color:white;"></i></a>
            </span>
            <h4 class="card-title">{package_title}</h4>
            <h6 class="card-subtitle mb-2">{package_author}</h6>
            <h6 class="card-subtitle mb-3 text-muted">{package_version}</h6>
            <hr>
            <p class="card-text">{package_description}</p>
            <hr>
            <p class="card-subtitle mb-3">Dependencies: {deps}</p>
            <p class="card-subtitle mb-3">Conflicts: {conflicts}</p>
        </div>
      </div>"""
    entry = ""
    for i in range(len(list_of)):
        package_title = list_of[i][0]['name']
        package_author = list_of[i][0]['author']
        package_version = list_of[i][0]['version']
        package_description = list_of[i][0]['description']
        download_link = list_of[i][0]['download_link']
        deps = list_of[i][0]['dependencies']
        conflicts = list_of[i][0]['conflicts']
        entry += template.format(package_author=package_author, package_description=package_description, package_title=package_title, package_version=package_version, download_link=download_link, deps=deps, conflicts=conflicts)
    return entry
        
        
        