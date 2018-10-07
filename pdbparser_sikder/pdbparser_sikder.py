#!/usr/bin/env python

pdbfile = "1nap.pdb"
outputFile  = "sikder_output.txt"

with open(pdbfile) as p:
    type,num,atom,amino,chain,res,xs,ys,zs,occ,bs,elem = [],[],[],[],[],[],[],[],[],[],[],[]
    for line in p:
        if line[0:4] in ("ATOM", "HETA"):
            na,nu,at,am,ch,r,x,y,z,oc,b,e = line.split()
            type.append(na)
            num.append(nu)
            atom.append(at)
            amino.append(am)
            chain.append(ch)
            res.append(int(r))
            xs.append(float(x))
            ys.append(float(y))
            zs.append(float(z))
            occ.append(float(oc))
            bs.append(float(b))
            elem.append(e)
        else:
            pass

print("The possible chains are: ")
print(set(chain))
user_chain = input("Pick a chain: ").strip().upper()
utype,unum,uatom,uamino,uchain,ures,uxs,uys,uzs,uocc,ubs,uelem = [],[],[],[],[],[],[],[],[],[],[],[]

for i in range(0, len(type)):
    if atom[i].strip() in ("N", "CA", "C", "O"):
        utype.append(type[i])
    else:
        pass

#with open(outputFile, "w") as out:
    #out.write("Name\tNum\tAtom\tAmino\tChain\tResidue\tX Coord\tY Coord\tZ Coord\tOcc\tB\tElement\n")
    #for i in range(0, len(name)):
        #out.write(name[i] + "\t" + num[i] + "\t" + atom[i] + "\t" + amino[i] + "\t" + chain[i] + "\t" + res[i] + "\t" + xs[i] + "\t" + ys[i] + "\t" + zs[i] + "\t" + occ[i] + "\t" + bs[i] + "\t" + elem[i] + "\n")



