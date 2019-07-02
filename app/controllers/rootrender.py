import json


class RootRender:
    @staticmethod
    def generateLeaderboard():
        template = """\
          <a href="https://aptme.io/api/repo?search={link}"><h3 class="subtitle">{count}. {link}</h3>
          <h3 class="subtitle"><i class="fa fa-eye" style="margin-right: 1px;"></i> {vc}</h3></a>
          <hr>"""
        entry = ""
        count = 1
        with open('app/db/link_count.json', 'r+') as json_file:
            data = json.load(json_file)
            sortdict = [(k, data[k]) for k in sorted(data, key=data.get, reverse=True)]
            for k, v in sortdict:
                if len(k) >= 12:
                    if "hackyouriphone" not in k:
                        if "kiiimo" not in k:
                            if "xarold" not in k:
                                if "pulandres" not in k:
                                    if "https://cool" != k:
                                        entry += template.format(count=count, link=k.replace('https://', '').replace('http://', ''), vc=v)
                                        count += 1
        return entry