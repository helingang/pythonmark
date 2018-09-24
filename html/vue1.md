# Vue基础
- 基本传参和取值
    ```
    <div id="app">
        {{ message }}
    </div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app',
            data: {
                message: 'hello world'
            }
        })
        console.log(app.$data.message)
    </script>
    ```

- v-if条件语句和v-show显示语句
    ```
    <div id="app">
        <div class="login" v-if='isLogin1'>
            {{log}}
            <p v-if='isU'>你是本人</p>
            <p v-else>你是不本人</p>
        </div>
        <div class="login" v-else>
            你好,你未登录
            <p v-if='isU'>你是本人</p>
            <p v-else>你是不本人</p>
        </div>
        <div class="vip" v-show='isVip'>是会员</div>
    </div>

    <script>
        let app = new Vue({ // 实例化
            el: '#app', 
            data: {
                log: '你好,你已经登录',
                isLogin1: true, // 为false时标签被删除
                isU: false,
                isVip: true
            }, // 参数
        });
    </script>
    ```
- v-for循环语句和computed
    ```
    <div id="app">
        <ul>
            <li v-for='val in arr'>
                {{ val }}
            </li>
        </ul>
        <hr>
        <ul>
            <li v-for='val,index in sortArr'>
               {{index+1}}--{{val}}
            </li>
        </ul>
        <hr>
        <ul>
            <li v-for='(val,index) in sortObj'>
                {{index + 1}}--{{val.name}}--{{val.age}}
            </li>
        </ul>
    </div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                arr: [53,23,7,14,54,36,28],
                obj: [
                    {name: 'LostStars', age: '20'},
                    {name: 'Swifty', age: '31'},
                    {name: 'gangsi', age: '10'},
                    {name: 'husky', age: '22'}
                ]
            }, // 参数
            computed: {
                sortArr: function(){
                    return this.arr.sort(function(a, b){ 
                        return a - b 
                    })
                },
                sortObj: function(){
                    return this.obj.sort(function(a, b){ 
                        return a.age - b.age 
                    })
                }   
            }, // 改造data中的数据
        })

    </script>
    ```

- v-text和v-html
    ```
    <div id="app">
        <!-- 当script还未加载时span标签的innerHTML不会显示 -->
        <span>{{message}}</span><br> 
        <span v-text='message'></span>
        <!-- 减少此方法的使用,因为容易导致xss攻击 -->
        <span v-html='inner'></span>
    </div>

    <script>
        setTimeout(function () {
            var app = new Vue({ // 实例化
                el: '#app',
                data: {
                    message: 'hello world',
                    inner: '<h1>Hello World</h1>'
                }, // 参数
            })
        }, 1000)
    </script>
    ```

- v-on & @click绑定事件
    ```
    <div id="app">
        比赛分数 <span v-text='baseScore'></span><br>
        <!-- 绑定鼠标点击事件 -->
        <button v-on:click='addScore'>得分1
        <button @click='addScore'>得分1(用@符绑定)
        <!-- 绑定回车抬起事件 -->
        <button v-on:keyup.13='addScore2'> 得分2(用回车符绑定)
    </div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                baseScore: 0,
                score1: 1,
                score2: 2
            }, // 参数
            methods: {
                addScore: function(){
                    this.baseScore += this.score1;
                },
                addScore2: function(){
                    this.baseScore += this.score2;
                }
            }
        })
    </script>
    ```

- v-model数据绑定
    ```
    <h3>绑定文本框</h3>
    <span>原始数据: {{showData}}</span>
    <br/>
    v-model&nbsp;<input type="text" v-model='showData'>
    <br/>
    v-model.number&nbsp;<input type="text" v-model.number='showData'>
    <br/>
    v-model.trim&nbsp;<input type="text" v-model.trim='showData'>
    <br/>
    v-model.lazy&nbsp;<input type="text" v-model.lazy='showData'>

    <h3>绑定文本域</h3>
    <textarea name="" id="" cols="30" rows="2" v-model='showData'></textarea>

    <h3>多选按钮绑定一个值</h3>
    <input type="checkbox" v-model='boolean'>&nbsp;{{boolean}}

    <h3>多选按钮绑定数组</h3>
    <input type="checkbox" id="name1" value='Sam' v-model='nameArr' checked="checked">
    <label for="name1">Sam</label>
    <input type="checkbox" id="name2" value='Jack' v-model='nameArr'>
    <label for="name2">Jack</label>
    <input type="checkbox" id="name3" value='mai' v-model='nameArr'>
    <label for="name3">mai</label>
    <div>您选中的姓名有 <span v-for='val,index in nameArr'>{{val}} </span></div>
    <div>您选中的姓名有 {{nameArr}}</div>

    <h3>单选按钮绑定数据</h3>
    <input type="radio" id='food1' value='苹果' name="fruit" v-model='fruitName' checked>
    <label for="food1">苹果</label>
    <input type="radio" id='food2' value='香蕉' name="fruit" v-model='fruitName'>
    <label for="food2">香蕉</label>
    <input type="radio" id='food3' value='桃子' name="fruit" v-model='fruitName'>
    <label for="food3">桃子</label>
    <div>您选中的水果是 {{fruitName}}</div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                showData: '12345',
                boolean: true,
                nameArr: [],
                fruitName: ''
            }, // 参数
        })
    </script>
    ```

- v-bind数据绑定
    ```
    <div id="app">
        <h3>处理href和src属性</h3>
        <p>
            <img v-bind:src="imgSrc" alt="" width=200px>
        </p>
        <p>
            <a :href="aHref" target='_blank'>www.bilibili.com(使用:缩写绑定)</a>
        </p>
        <h3>绑定CSS样式</h3>
        <div :class='className'>1. 直接绑定className</div>
        <div :class='{div2: boolean}'>2. 通过布尔值判断是否绑定某一个class</div>
        <div :class='[div1,div2]'>3. 绑定多个class名</div>
        <div :class='boolean?div1:div2'>4. 通过布尔值判断绑定两个class中的哪一个</div>
        <div :style='{color: yellow}'>5. 绑定具体的style属性</div>
        <div :style='styleObj'>6. 绑定整个style对象</div>
    </div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                imgSrc: 'https://i0.hdslb.com/bfs/archive/bdb288021ff854d3ac618ac8c1eafd300ec9ed9b.png',
                aHref: 'https://www.bilibili.com/',
                boolean: true,
                className: 'div1',
                div1: 'div1',
                div2: 'div2',
                yellow: 'green',
                styleObj: {
                    fontSize: '30px',
                    color: 'purple'
                }
            }, // 参数
        })
    </script>
    ```

- 其他
    ```
    <div id="app">
        <div>原始数据: {{message}}</div>
        <div v-pre>v-pre不进行渲染 {{message}}</div>
        <div v-cloak>v-cloak渲染完成后才显示 {{message}}</div>
        <div v-once>v-once只渲染一次 {{message}}</div>
        <input type="text" v-model='message'>
    </div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app',
            data: {
                message: 'hello world'
            }, // 参数
        })
    </script>
    ```