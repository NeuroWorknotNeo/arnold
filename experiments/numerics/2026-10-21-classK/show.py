import json,sys
for ex in sys.argv[1:]:
    r=json.load(open('out/%s.json'%ex))
    print('=====',ex,'m=',r['m'],'degrees',r['parts_degrees'],'u_m=',r['u_m'],'sos_ok',r['sos_certificate_ok'])
    for c in r['components']:
        print(' --',c['name'], {k:c[k] for k in ('kind','MB','MB_on_component','H','H_real_roots','j','g_j','g_j_float') if k in c})
        if 'G' in c: print('    G =',c['G'])
        if 'G_value' in c: print('    G const =',c['G_value'])
        for q in c.get('crit',[]):
            print('    crit %-8s G=%s G\'\'=%s G\'\'+jG=%s mult=%s %s omega=%s'%(q['t'][:8],q['G'][:10],q['d2G'][:10],(q['G2_plus_jG'] or 'None')[:10],q['mult'],q['kind'],q['omega']))
        if 'g_unit' in c and 'j' in c and c.get('j') is None: print('    g_unit', c['g_unit'])
