function stp() {
    var req = getXmlHttp()

    var targetElem = document.getElementById('tableData')

    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            if(req.status == 200) {
                var res = JSON.parse(req.responseText);
                sx = parseInt(res.sx);
                sy = parseInt(res.sy);
                sz = parseInt(res.sz);
                arr = res.arr;
                storg_site = res.storg_site;
                stremote = res.stremote


                txtremote = 'Отправлены на удаленный склад: '
                for (var i = 0; i < stremote.length; i++) {
                  txtremote = txtremote + stremote[i] + ', '
                }
                alert(txtremote);


                (document.querySelector('input.name')).setAttribute('disabled', '');
                (document.querySelector('input.x')).setAttribute('disabled', '');
                (document.querySelector('input.y')).setAttribute('disabled', '');
                (document.querySelector('input.z')).setAttribute('disabled', '');
                (document.querySelector('input.mass')).setAttribute('disabled', '');
                (document.getElementById('inputform')).setAttribute('hidden', 'true');

                var infoLabel = document.createElement('table');

                var tbl = document.createElement('table');
                tbl.setAttribute('border', '2');
                tbl.setAttribute('class', 'main_table');

                var tbdy = document.createElement('tbody');

                for (var i = 0; i < sy; i++) { // rows

                    var tr = document.createElement('tr');
                    tr.style.height = '100px';
                    for (var j = 0; j < sx; j++) { // columns
                        var td = document.createElement('td');
                        td.style.width = '100px';
                        if(arr[i][j] == 1) {
                            td.setAttribute('rowspan', '2')
                        }
                        if(arr[i][j] == 2) {
                            td.setAttribute('colspan', '2')
                        }
                        if(arr[i][j] == 3) {
                            td.setAttribute('rowspan', '2');
                            td.setAttribute('colspan', '2');
                        }
                        if(arr[i][j] == 4) {
                            continue;
                        }
                        tr.appendChild(td)

                    }
                    tbdy.appendChild(tr);
                }
                tbl.appendChild(tbdy);
                targetElem.appendChild(infoLabel);
                targetElem.appendChild(tbl);

                document.getElementById('div_storg').removeAttribute('hidden');
                var storg = document.createElement('table');
                var tr0 = document.createElement('tr');
                var td = document.createElement('th');
                var butt = document.createElement('button');
                td.innerHTML = 'Название товара';
                tr0.appendChild(td.cloneNode(true));
                td.innerHTML = 'Занимаемые ячейки';
                tr0.appendChild(td.cloneNode(true));
                td.innerHTML = 'Нажмите, чтобы отправить запрос';
                td.setAttribute('class', 'td');
                tr0.appendChild(td.cloneNode(true));
                storg.setAttribute('id', 'storg_table');
                storg.appendChild(tr0.cloneNode(true));
                document.getElementById('div_storg').appendChild(storg.cloneNode(true));



                for (var i = 0; i < (storg_site.length); i++) {
                  var td = document.createElement('td')
                  td.setAttribute('class', 'td')
                  var tr = document.createElement('tr')
                  tr.setAttribute('class','td')
                  td.innerHTML = (storg_site[i])[1]
                  tr.appendChild(td.cloneNode(true))


                  td.innerHTML = storg_site[i][2]
                  tr.appendChild(td.cloneNode(true))


                  var butt = document.createElement('button')
                  butt.setAttribute('onclick', 'gtpos(this)')
                  butt.setAttribute('value', 'Отправить запрос на выдачу')
                  butt.setAttribute('class', 'get-button')
                  td.innerHTML = ''
                  td.appendChild(butt.cloneNode(true))
                  tr.appendChild(td.cloneNode(true))

                  document.getElementById('storg_table').appendChild(tr.cloneNode(true));
                }

            }
        }
      }

    req.open('GET', '/gettable', true);

    req.send(null);
}
function getXmlHttp(){
      var xmlhttp;
      try {
        xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
      } catch (e) {
        try {
          xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (E) {
          xmlhttp = false;
        }
      }
      if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
        xmlhttp = new XMLHttpRequest();
      }
      return xmlhttp;
    }


    function snd() {
        if (((document.querySelector('input.name')).value != "") &&
        ((document.querySelector('input.x')).value != "") &&
        ((document.querySelector('input.y')).value != "") &&
        ((document.querySelector('input.z')).value != "") &&
        ((document.querySelector('input.mass')).value != "")) {

        const nodet = document.createElement('tr');
        var node = document.createElement('td');
        document.getElementById('naklad').appendChild(nodet);

        node.innerHTML = (document.querySelector('input.name')).value;
        nodet.appendChild(node.cloneNode(true));


        node.innerHTML = (document.querySelector('input.x')).value;
        nodet.appendChild(node.cloneNode(true));


        node.innerHTML = (document.querySelector('input.y')).value;
        nodet.appendChild(node.cloneNode(true));


        node.innerHTML = (document.querySelector('input.z')).value;
        nodet.appendChild(node.cloneNode(true));


        node.innerHTML = (document.querySelector('input.mass')).value;
        nodet.appendChild(node.cloneNode(true));

        let a = 'http://127.0.0.1:3000/?name=' + document.querySelector('input.name').value +
                    '&x=' + document.querySelector('input.x').value +
                    '&y=' + document.querySelector('input.y').value +
                    '&z=' + document.querySelector('input.z').value +
                    '&mass=' + document.querySelector('input.mass').value
        var request = new XMLHttpRequest();
        request.open('get', a, true)
        request.send()

       }
       else {
       alert('Заполните все поля!')
       }
      }



function gtpos(ths) {
    tr = ths.parentNode.parentNode
    getdest = tr.getElementsByTagName('td')[1].innerHTML
    var inPut = getdest.split(', ')
    if (inPut != []) {
    request = new XMLHttpRequest();
    console.log(inPut)
    request.open('post', '/position?dest=' + inPut, true);


    request.onreadystatechange = function() {
        if (request.readyState == 4) {
            console.log(request.status)
            if(request.status == '200') {
                alert('Товар выдан успешно!')
            }
            if(request.status == '404') {
                alert('Введенная ячейка пуста')
            }
            if(request.status == "400") {
                alert('Введенной ячейки не существует')
            }

    }
    }
    request.send();
    tr.setAttribute('hidden', '')
   }
}
