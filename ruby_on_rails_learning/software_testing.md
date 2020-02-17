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

## 如何用现有的工具为java程序生成控制流图
- Soot
- https://sable.github.io/soot

# 数据流测试Data Flow Coverage
- try to ensure that values are computed and used correctly (关于点上的数据是否计算准确)
- Definition(def):常见的有赋值，初始化
- Use: a location where a variable is accessed比如说分支，判断，赋值的右边，循环

## sets of def & use
- def(n) or def(e)
The set of variables that are defined by node n or edge e
- use(n) or use(e)
The set of variables that are used by node n or edge e

## Du Pair
a pair of locations(li, lj)such that a variable v is defined at li and used at lj

## Def-clear
从li -> lj之间的定义没有被任意的其他节点定义过
### reach
If there is a def-clear path from li to lj with respect to v, the def of v at li reaches the use at lj

## Du Path
- du-path - a simple subpath that is def-clear with respect to v from a def of v to a use of v
- du(ni, nj, v) the set of du-paths from ni to nj
- du(ni, v) the set of du-paths that start at ni

## 三种覆盖准则
- (ADC) All-defs coverage -所有定义过的地方都覆盖过一次
- (AUC) All-uses coverage -关于变量v所有引用，使用的地方都覆盖过一次
- *注意,有引用，前面一定有定义
- (ADUPC) All-du-paths coverage - For each set S = du(ni, nj, v), TR contains every path d in S