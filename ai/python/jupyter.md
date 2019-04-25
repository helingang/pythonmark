## `Letex`
### 数学公式
- [参考文档](http://www.mohu.org/info/lshort-cn.pdf)
1. `\frac{1}{2}`分号
2. `\infty`无穷
3. `\sum_{i=0}^\infty`求和
4. `\binom{5}{3}`概率(5/3)
5. `{n \choose k}`概率(5/3)
6. `\mathop{\lim}_{n \to \infty }f(x)`极限
7. `sqrt{3}`根号
8. `\left( f(x) \right)`左右大括号
9. `$f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left(\frac{(x-\mu)^2}{2\sigma^2}\right)$`

### Magic开关
1. line magic (针对全局)
    - `%whos`
    - `%confing`
    - `%reset`
    - `%debug`调试
    - `%pdb on`出现错误直接进入调试

2. cell magic ( 针对当前cell)
    - `%%timeit 50` 循环执行50次
    - `%%time`
    - `%%javascript` 执行下面的js代码
    - `%%html` 执行下面的html代码
    - `%%system` 调用下面的系统命令 (!直接加命令同理)
