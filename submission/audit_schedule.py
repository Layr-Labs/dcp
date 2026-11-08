"""Finite exact checks of the changed SPQ-14021 schedule; not proof certification."""
from fractions import Fraction as F
import json

def ceildiv(a,b): return (a+b-1)//b
A,B,D,W=F(1341,10000),F(10868,10000),F(3152,10000),F(999,2000)
assert A*W+B*D+B*B/2 == F(100010943,100000000)
assert A*W+B*D+B*B/2 > F(10001,10000)
assert F(65,41)*A+B == F(532753,410000) < F(6497,5000)
assert B+D == F(701,500)
assert 3**41 < 2**65 and 3**53 > 2**84
assert F(2**20,10000) > F(1087,1000)*20+F(4483,1000)
assert F(1,10000) > F(2174,1000*2**20)

def check(r):
 ell=ceildiv(1341*r,10000);w=999*r//2000
 m=ceildiv(10868*r,10000);dl=ceildiv(3152*r,10000)
 kappa=(m-1).bit_length()+1
 assert w < m and dl>=kappa+1
 # Every pairing capacity equals w; exact sum of all tree capacities.
 tree=m*dl+F(m*m,2)+dl+F(m,2)-1-m*(kappa+1)
 assert tree.denominator==1
 assert ell*w+tree>=r*r
 assert ell<=F(135,1000)*r and m<=F(1087,1000)*r
 assert kappa+1<=(r-1).bit_length()+4
 assert F(65,41)*ell+m < F(6497,5000)*r+3
 assert m+dl<=F(701,500)*r+2
 assert w<=W*r
 assert F(701,500)*r-w >= 2*r.bit_length()
 # Bounds use log2 r <= bit_length(r), conservatively.
 assert F(7,10)*r >= 4*r.bit_length()+33

rs=set(range(2**20,2**20+10001))
for k in range(20,257):
 for offset in [-1,0,1,17,9999]:
  if 2**k+offset>=2**20: rs.add(2**k+offset)
for r in sorted(rs):check(r)
print(json.dumps({'schedule_cases':len(rs),'all_exact_checks_passed':True,'capacity_coefficient':str(A*W+B*D+B*B/2),'source_coefficient_upper':str(F(65,41)*A+B),'tree_coefficient':str(B+D)}))
