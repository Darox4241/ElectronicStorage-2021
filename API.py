#   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    #
#   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    #
#   @@@@@                                ##%%%#%                               &@@@@    #
#   @@@@@                      %%%%(((((((((((((((((((%%%%                     &@@@@    #
#   @@@@@                 %%((((((((((((((((((((((((((((((((#%%                &@@@@    #
#   @@@@@             .%(((((((((((((((((((((((((((((((((((((((((%             &@@@@    #
#   @@@@@           %(((((((((((((((((((((((((((((((((((((((((((((((%          &@@@@    #
#   @@@@@        ##(((((((((((((((((((((((((((((((((((((((((((((((((((%,       &@@@@    #
#   @@@@@      ,#(((((((((((((((((((((((((((&(((((((((((((((((((((((((((%      &@@@@    #
#   @@@@@     %((((((((((((((((((((((#@@@@@@@@@@@@@(((((((((((((((((((((((%    &@@@@    #
#   @@@@@    ((((((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((((((((((((((   &@@@@    #
#   @@@@@   ((((((((((((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((((((((((((  &@@@@    #
#   @@@@@  (((((((((((((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((((((((((((( &@@@@    #
#   @@@@@ #((((((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((((((((((%&@@@@    #
#   @@@@@ ((((((((((((((((((///&@@@@@@@@@@@@@@@@@@@@@@@@@&///((((((((((((((((((&@@@@    #
#   @@@@@#((((((((((((((&((((((((((///@@@@@@@@@@@@@///(((((((((((((((((((((((((@@@@@    #
#   @@@@@(((((((((((((((&@@@@@@((((((((((///////(((((((((#@@@@@@(((((((((((((((@@@@@    #
#   @@@@@/(((((((((((((((@@@@@@@@@@@@@(((((((((((((@@@@@@@@@@@@@(((((((((((((((@@@@@    #
#   @@@@@ ((((((((((((((((((///&@@@@@@@@@@@@@@@@@@@@@@@@@&///((((((((((((((((((&@@@@    #
#   @@@@@ ((((((((((((((&((((((((((///@@@@@@@@@@@@@///(((((((((((((((((((((((((&@@@@    #
#   @@@@@  (((((((((((((&@@@@@@((((((((((///////(((((((((#@@@@@@(((((((((((((( &@@@@    #
#   @@@@@   (((((((((((((@@@@@@@@@@@@@(((((((((((((@@@@@@@@@@@@@(((((((((((((  &@@@@    #
#   @@@@@    (((((((((((((((///&@@@@@@@@@@@@@@@@@@@@@@@@@&///(((((((((((((((   &@@@@    #
#   @@@@@     (((((((((((((((((((((///@@@@@@@@@@@@@///(((((((((((((((((((((    &@@@@    #
#   @@@@@       (((((((((((((((((((((((((///////(((((((((((((((((((((((((      &@@@@    #
#   @@@@@         (((((((((((((((((((((((((((((((((((((((((((((((((((((        &@@@@    #
#   @@@@@           (((((((((((((((((((((((((((((((((((((((((((((((((          &@@@@    #
#   @@@@@              (((((((((((((((((((((((((((((((((((((((((((             &@@@@    #
#   @@@@@                 /(((((((((((((((((((((((((((((((((((,                &@@@@    #
#   @@@@@                      /(((((((((((((((((((((((((                      &@@@@    #
#   @@@@@                                                                      &@@@@    #
#   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    #



from flask import Flask, request
import json
import simplejson
import requests
from operator import itemgetter
import uuid

base_url = 'http://127.0.0.1:5000'
response = requests.get(base_url + '/scheme')
response = response.json()

sx = response['size']['size_x']
sy = response['size']['size_y']
sz = response['size']['size_z']

merged_arr = response['merged']

Pos = []
num = 0

app = Flask(__name__, static_folder='')



@app.route('/', methods=['GET'])
def mult():
    if request.args['name'] != '':
        a = [(request.args['name']),
             (request.args['x']),
             (request.args['y']),
             (request.args['z']),
             (request.args['mass'])]
        a.reverse()
        a.append(str(uuid.uuid4()))
        a.reverse()
        Pos.append(a)
        return {"status": "ok"}, 200
    else:
        return {"status": "error"}, 405


@app.route('/gettable', methods=['GET'])
def get_table():
    arr = [[0 for i in range(sx)] for j in range(sy)]
    storg = []
    remote = []
    tkn = []

    for i in merged_arr:
        if len(i) == 4:
            arr[int(i[0][1:len(i)]) - 1][int(ord(i[0][0]) - int(ord('A')))] = 3
            for m in range(1, 4):
                arr[int(i[m][1:len(i)]) - 1][int(ord(i[m][0]) - int(ord('A')))] = 4
        else:
            if i[0][0] == i[1][0]:
                arr[int(i[0][1:len(i)]) - 1][int(ord(i[0][0]) - int(ord('A')))] = 1
                arr[int(i[1][1:len(i)]) - 1][int(ord(i[1][0]) - int(ord('A')))] = 4
            else:
                arr[int(i[0][1:len(i)]) - 1][int(ord(i[0][0]) - int(ord('A')))] = 2
                arr[int(i[0][1:len(i)]) - 1][int(ord(i[0][0]) - int(ord('A'))) + 1] = 4


    for i in Pos:
        px = int(i[2])
        py = int(i[3])
        pz = int(i[4])
        A = []
        A.append(px)
        A.append(py)
        A.append(pz)
        mx = 0
        for m in A:
            if mx < m < 1000:
                mx = m
        try:
            A.remove(mx)
        except ValueError:
            i.pop(3)
            i.pop(3)
            i[2] = 4
            continue
        px = A[0]
        py = A[1]
        i.pop(3)
        i.pop(3)
        if px > 2000 or py > 2000:
            i[2] = 4
        else:
            if px > 1000 and py > 1000:
                i[2] = 3
            elif px <= 1000 and py <= 1000:
                i[2] = 0
            else:
                i[2] = 1
    Pos1 = Pos.copy()


    Pos1.sort(key=itemgetter(2, 3), reverse=True)
    for i in Pos1:
            for y in range(sy - 1, -1, -1):
                for x in range(sx - 1, -1, -1):
                    cell = chr(x + ord('A')) + str(y + 1)
                    if cell not in tkn and i[0] not in tkn:
                        if arr[y][x] == i[2] == 3 or (
                                i[2] == 1 and (arr[y][x] == 1 or arr[y][x] == 2 or arr[y][x] == 3)):
                            storg.append([i[0], i[1], []])
                            tkn.append(i[0])
                            for mrg in merged_arr:
                                try:
                                    if mrg.index(cell) == 0:
                                        for cells in mrg:
                                            storg[-1][2].append(cells)
                                            tkn.append(cells)
                                except ValueError:
                                    continue
                        if i[2] == 0:
                            if arr[y][x] == 1 or arr[y][x] == 2 or arr[y][x] == 3:
                                storg.append([i[0], i[1], []])
                                tkn.append(i[0])
                                for mrg in merged_arr:
                                    try:
                                        if mrg.index(cell) == 0:
                                            for cells in mrg:
                                                storg[-1][2].append(cells)
                                                tkn.append(cells)
                                    except ValueError:
                                        continue
                            elif arr[y][x] == 0:
                                storg.append([i[0], i[1], [cell]])
                                tkn.append(cell)
                                tkn.append(i[0])
                                break
            else:
                if i[0] not in tkn:
                    remote.append(i[1])
                    tkn.append(i[0])

    storg_site = []
    for i in storg:
        sndid = i[0]
        snddst = i[2]
        snd = [{
            'uuid': sndid,
            'destination': snddst,
        }]
        snd_json = simplejson.dumps(snd)
        response = requests.post('http://127.0.0.1:5000/', snd_json, headers={"Content-Type": "application/json"})
        response = response.json()
        if response['status'] == 'ok':
            storg_site.append([i[0], i[1], i[2]])
    return json.dumps({
        'sx': sx,
        'sy': sy,
        'sz': sz,
        'arr': arr,
        'storg_site': storg_site,
        'stremote': remote,
    }), 200


@app.route('/position', methods=['POST'])
def get_item():
    inPut = request.args['dest']
    inPut = list(map(str, inPut.split(',')))
    dest = ({
        "destination": inPut,
    })
    response = requests.get(base_url + '/position', dest)
    response = response.json()
    if response['status'] == 'ok':
        return {"status": "ok"}, 200
    elif response['status'] == 'position is empty':
        return {"status": "position is empty"}, 404
    else:
        return {"status": "position does not exist"}, 400


if __name__ == '__main__':
    app.run(port=3000)
