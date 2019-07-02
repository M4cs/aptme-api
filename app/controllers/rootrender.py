import json


class RootRender:
    @staticmethod
    def generateLeaderboard():
        template = """\
          <a href="https://aptme.io/api/repos?search={link}"><h3 class="subtitle">{count}. {link}</h3></a>
          <hr>"""
        entry = ""
        count = 1
        with open('app/db/link_count.json', 'r+') as json_file:
            data = json.load(json_file)
            sortdict = [(k, data[k]) for k in sorted(data, key=data.get, reverse=True)]
            for k, v in sortdict:
                if len(k) >= 5:
                    entry += template.format(count=count, link=k)
                    count += 1
        return entry