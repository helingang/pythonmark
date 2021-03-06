# 决策树与随机森林
- 目录
    - 从lr到决策树
        - 总体流程与核心问题
        - 熵,信息增益,信息增益率
    - 回归树
        - 构建回归树
        - 最优化回归树
    - 从决策树到随机森林

- 总体流程
    <img src='./img/ml2-1.png'>
- 熵
    <img src='./img/ml2-2.png'>

    - 信息熵: 度量样本集合的纯度的指标
        - Ent取最大值时,不纯度最低,所有样本的比例相同
        - y表示有多少个类别(例如好瓜和坏瓜,类别就是2)
        - 机器学习的目的就是让不纯度降低
    - 信息增益(最佳划分属性选择)(ID3)
        <img src='./img/ml2-3.png'>

        - 得到的结果表示,不纯度有没有降低,降低了多少

        - 例子
            <img src='./img/ml2-4.png'>

            - 不确定度降低了0.109
            <img src='./img/ml2-5.png'>

            - 纹理的不纯度下降的最高,作为划分属性
            <img src='./img/ml2-6.png'>

            - 决策树
            <img src='./img/ml2-7.png'>
    - ID3的问题
        - 例如学号id的分叉
        - 信息增益率(ID4.5)
        <img src='./img/ml2-8.png'>

    - 选择划分属性选择,基尼系数(cart 二叉树)
        - gini越低,不纯度越低
        <img src='./img/ml2-9.png'>

- 三种树
    <img src='./img/ml2-10.png'>

- 决策树的含义
    <img src='./img/ml2-11.png'>

    - RSS表示预估结果的好坏
        - 尽量使RSS小
        - 左边的sigma表示有切割了多少块,右边的sigma表示每一块的误差
        <img src='./img/ml2-12.png'>

- 回归树
    - 递归二分
        - 自顶向下的贪婪式递归方案
        - 每一次在新的区域砍,而不管已经砍的区域
        <img src='./img/ml2-13.png'>
    - 回归树几种切割方式
        <img src='./img/ml2-14.png'>
    - 避免过拟合 添加正则项
        <img src='./img/ml2-15.png'>


- 随机森林
    <img src='./img/ml2-16.png'>
    <img src='./img/ml2-17.png'>

