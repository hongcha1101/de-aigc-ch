import re,sys,json,math,statistics
P={
"FEI_HUA":["\u503c\u5f97\u6ce8\u610f\u7684\u662f","\u4e0d\u53ef\u5426\u8ba4\u7684\u662f","\u4f17\u6240\u5468\u77e5","\u7839\u5f1b\u4e0d\u79fb\u7684\u662f","\u4e0d\u53ef\u5ffd\u89c6\u7684\u662f","\u9996\u5148\u9700\u8981\u660e\u786e\u7684\u662f"],
"WAN_NENG":["\u53d1\u6325\u7740\u8d8a\u6765\u8d8a\u91cd\u8981\u7684\u4f5c\u7528","\u626e\u6f14\u7740\u4e0d\u53ef\u6220\u7f3a\u7684\u89d2\u8272","\u5177\u6709\u6df1\u8fdc\u7684\u610f\u4e49","\u662f\u5f53\u52a1\u4e4b\u6025","\u523b\u4e0d\u5bb9\u7f13","\u65e2\u662f\u6311\u6218\u4e5f\u662f\u673a\u9047"],
"HEI_HUA":["\u8d4b\u80fd","\u95ed\u73af","\u6293\u624b","\u9897\u7c92\u5ea6","\u5e95\u5c42\u903b\u8f91","\u5012\u903c","\u6c89\u6dc0","\u62c9\u901a"],
"SI_ZI":["\u7efc\u4e0a\u6240\u8ff0","\u603b\u800c\u8a00\u4e4b","\u7531\u6b64\u53ef\u89c1","\u4e0e\u6b64\u540c\u65f6","\u4e0d\u53ef\u6216\u7f3a","\u81f3\u5173\u91cd\u8981","\u56de\u6839\u7ed3\u5e95"],
"JUE_DUI":["\u8bc1\u660e\u4e86","\u5145\u5206\u8bf4\u660e","\u5fc5\u7136\u5bfc\u81f4","\u6beb\u65e0\u7591\u95ee","\u5f7b\u5e95"],
"CONNECTOR":["^\u6b64\u5916","^\u800c\u4e14","^\u7136\u800c","^\u56e0\u6b64","^\u6240\u4ee5","^\u4ece\u800c","^\u8fdb\u800c"],
"JIA_JING":["\u5927\u91cf","\u4f17\u591a","\u663e\u8457\u63d0\u5347","\u660e\u663e\u6539\u5584","\u6709\u6548\u63d0\u5347"],
"BEI_DONG":["\u9700\u8981\u88ab","\u53ef\u4ee5\u88ab","\u5e94\u8be5\u88ab","\u503c\u5f97\u88ab"],
}
def scan(t):
    r={}
    for c,pl in P.items():
        h=[]
        for p in pl:
            for m in re.finditer(p,t,re.M):
                ln=t[:m.start()].count('\n')+1
                h.append({"p":p,"m":m.group()[:25],"l":ln})
        if h: r[c]={"n":len(h),"h":h[:5]}
    return r
def main():
    args=[a for a in sys.argv[1:] if a!='--json']
    json_mode='--json' in sys.argv
    t=open(args[0],encoding='utf-8').read() if args else sys.stdin.read()
    if not t.strip(): print("No input",file=sys.stderr);sys.exit(1)
    r=scan(t);tt=sum(d['n'] for d in r.values())
    if json_mode:
        cats={c:{"count":d["n"],"hits":[{"pattern":h["p"],"match":h["m"],"line":h["l"]} for h in d["h"]]} for c,d in r.items()}
        verdict="PASS" if tt==0 else "LIGHT" if tt<=3 else "MODERATE" if tt<=8 else "HEAVY"
        print(json.dumps({"total":tt,"verdict":verdict,"categories":cats},ensure_ascii=False,indent=2))
        return
    print(f"Total AI pattern hits: {tt}")
    if tt==0:print("Verdict: PASS")
    elif tt<=3:print("Verdict: LIGHT")
    elif tt<=8:print("Verdict: MODERATE")
    else:print("Verdict: HEAVY")
    for c, d in sorted(r.items(),key=lambda x:-x[1]['n']):
        print(f"  [{c}] {d['n']}")
        for h in d['h'][:3]:print(f"    L{h['l']}: {h['m']}")
if __name__=='__main__':main()