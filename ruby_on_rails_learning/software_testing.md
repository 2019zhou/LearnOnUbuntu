# 结构化测试
## Vertex Coverage(VC)
## Edge Coverage(EC)
- 满足EC -> 满足VC
- 但满足边覆盖不代表满足点覆盖

## Covering Multiple Edges
- 是指相邻的两条边
- Edge-Pair Coverage(边对覆盖)(**EPC**)
- Complete Path Coverage(CPC): TR contains all paths in G
- n-Path Coverage(nPC): TR contains each reachable path of length up to n, inclusive, in G
- VC(n = 0) , EC(n = 1), EPC(n = 2), CPC(n = \utimate)
- 为了测试的完整性，解释的统一，定义是 <= n 的所有路径

## Subsume 蕴含
- C1 subsumes C2, denoted by C1 >= C2: **For any T, if T satisfies C1 implies T satisfies C2.**
- n1PC >= n2PC if n1>= n2
- C1 >= C2 does not imply that T1 satisfying C1 can detect any fault detected by T2 which satisfies C2.


# Control Flow Graph(控制流图)
- 是指程序执行的流转过程
- Vertex: Statement;Block;Function;Module
- Edge: Flow;Jump;Call
