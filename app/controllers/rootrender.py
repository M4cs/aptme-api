import json


class RootRender:
    @staticmethod
    def generateLeaderboard():
        template = """\
      <div class="card">
        <div class="card-body text-center">
          <h4 class="subtitle">{count}. {link}</h4>
        </div>
      </div>"""
        entry = ""
        count = 1
        with open('app/db/link_count.json', 'r+') as json_file:
            data = json.load(json_file)
            sortdict = [(k, data[k]) for k in sorted(data, key=data.get, reverse=True)]
            for k, v in sortdict:
                entry += template.format(count=count, link=k)
        return entry