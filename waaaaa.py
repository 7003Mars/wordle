globals().update(g_=globals(),l_=locals,r=__import__('requests',globals()),c=chr,cg='\x1b[0;37;42m',cy='\x1b[0;37;43m',ce='\x1b[0m',ec=set(),wc=set(),a=0,gs='',gl=lambda:(g_.update(gs=input('Guess:'))or(0 if(len(gs)==ln and('title' not in r.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+gs).json()))else gl())),ll=lambda:((g_.update(a=g_['a']+1)or gl()or print(''.join([((ec.add(gl)or cg+gl+ce)if gl==wl else((wc.add(gl)or cy+gl+ce)if gs.count(gl,0,i)<wd.count(gl)else gl))for i,(wl, gl)in enumerate(zip(wd,gs))]+[' ']+[(cg if c(i) in ec else(cy if c(i) in wc else''))+c(i)+ce for i in range(97,123)]))or ll())if gs!=wd else(print('You win!Attempts:',a)or 1)))or(lambda ip:g_.__setitem__('ln',(int(ip)if ip.isdigit()and(4<int(ip)<15)else 5))or g_.__setitem__('wd',r.get(f'https://random-word-api.herokuapp.com/word?number=1&length={ln}').json()[0]))(input("Word length?(5-14) Default:5\n"))or ll()
