# Vue
## 内部指令
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

## 全局API
- 自定义指令:directive
    ```
    <div id="app">
        <div v-ls='color'>{{num}}</div>
        <button v-on:click='addNum'>+1</button>
        <button onclick='fn()'>解绑</button>
    </div>

    <script>
        
        let fn = () => {
            app.$destroy();
        };
        Vue.directive('ls',{
            // 只调用一次,指令第一次绑定到元素时调用
            bind: function(el, binding, vnode){
                // el指DOM元素(这里是div)
                // binding.value指绑定的值({color1: ,color2...})
                // binding.name指自定义指令的名称(ls)
                // binding.expression指绑定的表达式(color)
                el.style.color = binding.value.color1;
                console.log('1 - bind');
            },
            //被绑定元素插入父节点时调用(父节点存在即可,不必存在于document中)

            inserted: function(){
                console.log('2 - inserted');
            },

            //被绑定于元素所在模板更新时调用,而无论绑定值是否变化,通过比较更新前后的绑定值,可以忽略不必要的模板更新

            update: function(el,binding){
                el.style.color = binding.value.color2;
                console.log('3 - update');   
            },

            //被绑定元素完成更新时调用
            componentUpdated: function(){
                console.log('4 - componentUpdated');
            },
            //只调用一次,指令与元素解绑时调用
            unbind: function(el,binding){
                el.style.color = binding.value.color3;
                console.log('5 - unbind');
            }
        });
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                num: 0,
                color: {
                    color1: 'red',
                    color2: 'purple',
                    color3: 'pink'
                }
                    
            }, // 参数
            methods: {
                addNum: function(){
                    this.num++
                }
            }
        })
    </script>
    ```

- 扩展实例构造器:Vue.extend
    ```
    <div id="name1"></div>
    <p class="name2"></p>
    <author></author> 

    <a href="../index.html">回到首页</a> 
    <script>
        // Vue.extend 返回的是一个“扩展实例构造器”,也就是预设了部分选项的Vue实例构造器。经常服务于Vue.component用来生成组件，可以简单理解为当在模板中遇到该组件名称作为标签的自定义元素时，会自动调用“扩展实例构造器”来生产组件实例，并挂载到自定义元素上
        var nameExtend = Vue.extend({
            data: function(){
                return {
                    name: 'LostStars',
                    nameHref: 'http://www.baidu.com'
                }
            },
            template: '<p><a :href="nameHref" target=\'_blank\'>{{name}}</a></p>',
            
        });

        new nameExtend().$mount('#name1');
        new nameExtend().$mount('.name2');
        new nameExtend().$mount('author');

    </script>
    ```

- 全局操作:Vue.set
    ```
    <div id="app">
        {{ message.data1 }}
        <button onclick='fn()'>add</button>
        <ul>
            <li v-for='(value, index) in message.data2'>
                {{ value }}
            </li>
        </ul>
    </div>

    <script>
        function fn(){
            // Vue.set(app.message,'data1',10)
            // app.message.data1++;
            // app.message.data2[2] = 'zz'; // 如果只执行这一行,则不会成功,而改用Vue.set则可以成功
            Vue.set(app.message.data2, 2, 'zz');
            Vue.set(app.message, 'data1', 20);
        }

        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                message: {
                    data1: 5,
                    data2: ['aa', 'bb', 'cc']
                }
            } // 参数
            
        });

    </script>
    ```

- 生命周期
    ```
    <div id="app">
        {{ num }}
        <p><button v-on:click='add'>add</button></p>
        <p><button onclick='app.$destroy()'>销毁</button></p>
    </div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                num: 1
            }, // 参数
            methods: {
                add: function(){
                    this.num++
                }
            },
            beforeCreate: function(){
                console.log('1-beforeCreate 创建之前');
            },
            created: function(){
                console.log('2-created 创建之后');
            },
            beforeMount: function(){
                console.log('3-beforeMount 挂载之前');
            },
            mounted: function(){
                console.log('4-mounted 挂载之后');
            },
            beforeUpdate: function(){
                console.log('5-beforeUpdate 数据更新前');
            },
            updated: function(){
                console.log('6-updated 被更新后');
            },
            activated: function(){
                console.log('7-activated');
            },
            deactivated: function(){
                console.log('8-deactivated');
            },
            beforeDestroy: function(){
                console.log('9-beforeDestroy 销毁之前');
            },
            destroyed: function(){
                console.log('10-destroyed 销毁之后')
            }
        })
    </script>
    ```

- 模板:template
    ```
    <div id="app">
        {{ message }}
    </div>
    
    <hr>
    <a href="../index.html">回到首页</a>

    <template id='temp2'>
        <h4><a href='#'>我是template模板</a></h4>
    </template> 
    
    <script type="x-template" id='temp3'>
        <h4><a href='#'>我是script模板</a></h4>
    </script>

    <script>
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                message: 'hello world'
            }, // 参数
            // template: `
            //     <h4><a href='#'>span我是选项模板</a></h4>
            // `
            template: '#temp2' // 拥有template属性后template替换原来的#app中的内容
        })
    </script>
    ```

- 设置全局和局部组件:Vue.component
    ```
    <div id="app">
        <test></test>
    </div>
    <div id="app2">
        <test2 :num='num'></test2>
        <test3></test3>
        <ls></ls>
        {{num}}
    </div>

    <script>
        Vue.component('test',{
            template: `<h4 style='color: pink'>这里是全局组件</h4>`
        })
        Vue.component('ls',{
            template: `<span>ls组件</span>`
        })
        var app = new Vue({ // 实例化
            el: '#app',
        });
        var app2 = new Vue({ // 实例化
            el: '#app2',
            data: {
                num: 12
            },
            components: {
                 test2: {
                    template: '<h4 style="color: pink">这里是局部组件test2 {{ num }} </h4>',
                    props: {
                        num: {
                            type: Number,
                            require: true
                        }
                    }
                },
                test3: {
                    template: `<h4 style='color: pink'>这里是局部组件test3</h4>`
                }
            }
        })
    </script>

    ```
- 设置组件的props属性:Vue.component
    ```
    <div id="app">
        <dev :say='message'></dev>
        <dev :info="l1"></dev>
    </div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                message: 'hello world',
                data: {
                    'a': 100,
                    'b': 200
                },
                l1: [15, 20, 25]
            }, // 参数
            components: {
                dev: {
                    template: `<h4>我是web,说 {{ say }},{{ info }}</h4>`,
                    props: {
                        say: {
                            type: String,
                            require: true
                        },
                        info: {
                            type: Number,
                            require: true
                        }
                    }
                }
            }
        })
    </script>
    ```

- 设置父子组件:Vue.component
    ```
    <div id="app">
        <test1 :test1p='p1'></test1>
    </div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                p1: 1,
                p2: 2
            },
            components: {
                'test1': {
                    template: `
                    <div>
                        <span>父级{{ test1p }}</span>
                        <test2></test2>
                    </div>
                    `,
                    props: {
                        test1p: {
                            type: Number,
                            require: true
                        }
                    },
                    components: {
                        'test2': {
                            template: '<div>子级</div>',
                        }
                    }
                }
            }
        })
    </script>
    ```

- vue自带的component组件:Vue.component
    ```
    <div id="app">
        <component :is='who'></component>
    </div>

    <script>
        var componentA = {
            template: `<div>componentA</div>`
        };

        var componentB = {
            template: `<div>componentB</div>`
        };

        var componentC = {
            template: `<div>componentC</div>`
        };

        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                who: 'aa'
            }, // 参数
            components: {
                aa: componentA,
                bb: componentB,
                cc: componentC
            },
            created(){
                console.log(this.who)
            }
        })
    </script>
    ```

## 构造器中的选项
- 全局扩展时传递数据:propsData
    ```
    <ls></ls>

    <script>
        let j = {
            a: 'LostStars'
        };
        let ex = Vue.extend({
            template: `<span>{{ show }} {{ a }}</span>`,
            data: function(){
                return {
                    show: '我的名字是:'
                }
            },
            props: {
                'a': {
                    type: String,
                    require: true
                }
            }
        });

        new ex(
            {
                propsData: j // propsData用在全局扩展时进行传递数据
            }
        ).$mount('ls'); // 绑定到ls标签,也可以使用#ls绑定到id为ls的标签
    </script>
    ```

- 计算选项:computed
    
    ```
    计算选项多用于输出之前(不会污染data中的原始数据,在computed中进行改造)对原数据进行改造输出( 改造输出:包括格式的编辑,大小写转换,顺序重排,添加符号 )
    <div id="app">
        价格是: {{ newPrice }}
        <ul>
            <li v-for='value in reserveNews'>
                {{ value.data }}
            </li>
        </ul>
    </div>

    <script>
        var newsList = [
            { data: '习近平同金正恩举行会谈  向缅甸总统温敏致贺电', time: '2018/3/12' },
            { data: '人民日报评论：把中朝友谊发展得更好 新华社评论', time: '2018/3/13' },
            { data: '习近平主席特别代表杨洁篪将访问韩国', time: '2018/3/15' },
            { data: '汪洋：各专委会要进一步完善协商议政格局', time: '2018/3/16' },
        ];
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                price: 100,
                newsList: newsList

            }, // 参数
            computed: {
                newPrice: function(){
                    let str = `$ ${this.price} 元`;
                    return str
                },
                reserveNews: function(){
                    return this.newsList.reverse();
                }
            }
        })
    </script>
    ```

- 计算选项和方法:computed + methods
    ```
    <div id="app">
        <p>{{ temf }}</p>
        <p>{{ hefpf }}</p>
        <button @click='add'>add</button>
        <button @click='red'>red</button>
    </div>

    <script>
        var help = ['羽绒服', 'T恤', '长袖'];
        var tem = 10;
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                tem: tem,
                help: help
            }, // 参数
            computed: {
                temf: function(){
                    return '今日温度:' + this.tem
                },
                hefpf: function(){
                    let str = '穿衣建议:';
                    if ( this.tem > 15 ) {
                        return str + this.help[1]
                    } else if ( this.tem > 5 ){
                        return str + this.help[2]
                    } else {
                        return str + this.help[0]
                    }
                }
            },
            methods: {
                add: function(){
                    this.tem ++;
                },
                red: function(){
                    this.tem --;
                }
            }
        })
    </script>
    ```


- 方法: methods
    ```
    <div id="app">
        {{num}}
        <!-- 事件函数的 $event 对象 -->
        <p>
            <button v-on:click='add(num1, $event)'>原生按钮</button>
        </p>
        <p>
            <btn @click.native='add(num1, $event)'></btn>
        </p>
    </div>
    <button onclick='app.add(app.num1, event)'>Vue对象外部的按钮</button>

    <script>
        var btn = {
            template: '<button>组件按钮</button>'
        };
        var n = 5;
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                num: 1,
                num1: n
            }, // 参数

            components: {
                'btn': btn
            },

            methods: {
                add: function(a, b){
                    console.log(b);
                    a ? this.num += a : this.num ++;
                }
            }
        })
    </script>
    ```

- 监控属性(监控data中的数据):watch
    ```
    <div id="app">
        <p>今日温度: {{ tem }} C°</p>
        <p>穿衣建议: {{ clo }}</p>
        <p>
            <button @click='add'>add</button>
            <button @click='red'>red</button>
        </p>
    </div>

    <script>
        var c = ['T恤','长袖','毛衣','羽绒服',''];
        var app = new Vue({ // 实例化
            el: '#app',
            data: {
                tem: 14,
                clo: c[2]
            }, // 参数
            methods: {
                add: function(){
                    this.tem += 2;
                },

                red: function(){
                    this.tem -= 2;
                }
            },
            watch: {
                // tem: function(newV, oldV){
                //     let a;
                //     if (newV > 20) {
                //         a = 0;
                //     } else if (newV > 10) {
                //         a = 1;
                //     } else if (newV > 5) {
                //         a = 2;
                //     } else {
                //         a = 3;
                //     }
                //     this.clo = c[a]
                // }
            }
        });
        app.$watch('tem', function(newV, oldV){
            let a;
            console.log('newV', newV);
            console.log('oldV', oldV);
            if (newV > 20) {
                a = 0;
            } else if (newV > 10) {
                a = 1;
            } else if (newV > 5) {
                a = 2;
            } else {
                a = 3;
            }
            this.clo = c[a]
        })
    ```

- 混入:mixins
    ```
    Mixins一般有两种用途：
    1. 在你已经写好了构造器后，需要增加方法或者临时的活动时使用的方法，这时用混入会减少源代码的污染
    2. 很多地方都会用到的公用方法，用混入的方法可以减少代码量，实现代码重用

    <div id="app">
        {{num}}
        <p><button @click='add'>add</button></p>
    </div>
    <div id="app2">
        {{ num1 }}
        <p><button @click='add'>add</button></p>
    </div>

    <script>
        var csN = {
            data: {
                num: 2
            },
            updated: function(){ console.log('我是局部的混入; 改变后的数字为' + app.num) }
        };

        var csNG = {
            updated: function(){ console.log('我是全局的混入; 改变后的数字为' + app.num) }
        };

        // Vue.mixin(csNG)
        Vue.mixin({
            updated: function(){ console.log('我是全局的混入; 改变后的数字为' + app.num) }
        });

        var app = new Vue({ // 实例化
            el: '#app',

            data: {
                num: 1
            }, // 参数

            methods: {
                add: function(){
                    this.num ++
                }
            },

            updated: function(){
                console.log('原生的update生命周期; 改变后的数字为' + this.$data.num)
            },

            // 混入的先执行
            mixins: [csN],
        });

        var arr2 = new Vue({
            el: '#app2',
            data: {
                num1: 1
            },
            methods: {
                add: function () {
                    this.num1 ++;
                }
            }
        })
    </script>
    ```

- 扩展:extends 和自定义插值
    ```
    扩展的对象只能有一个
    可以扩展data,methods,生命周期函数等

    <div id="app">
        -[num]
        <p><button @click='add'>add</button></p>
    </div>

    <script>
        var extend = {
            data: {
                // 被原生的num覆盖
                num: 2,
                num1: 10
            },
            methods: {
                // 不会执行(被原生的add覆盖)
                add: function(){
                    console.log('我是扩展的add方法');
                    this.num += 10
                }
            },
            updated: function(){
                console.log('我是扩展的update方法');
            }
        };

        var app = new Vue({ // 实例化
            el: '#app',

            data: {
                num: 1
            }, // 参数

            methods: {
                add: function(){
                    console.log('我是原生的add方法');
                    this.num ++
                }
            },

            updated: function(){
                console.log('我是原生的update方法');   
            },

            // 只能扩展一个
            extends: extend,

            // 自定义插值形式
            delimiters: ['-[',']']
        })
    </script>
    ```

## 实例与内置组件
- 引入jq和调用构造器内部方法
    ```
    <div id="app">
        {{message}}
    </div>

    <script>
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                message: 'hello world'
            }, // 参数
            //在被挂载之后使用jq进行dom操作
            mounted: function(){
                $('#app').css({
                    width: 100,
                    height: 200,
                    backgroundColor: 'red'
                });
            },

            methods: {
                fn1: function(){
                    console.log('调用了构造器里面的方法');
                }
            }
        });

        // 调用构造器里面的方法
        setTimeout(function () {
            app.fn1();
        }, 1000)
    </script>
    ```

- $mount() $destroy() $forceUpdate $nextTick
    ```
    <div id="app"></div>
    <p>
        <button onclick='mount()'>mount</button>
        <button onclick='forceUpdate()'>forceUpdate</button>
        <button onclick='nextTick()'>nextTick</button>
        <button onclick='destroy()'>destroy</button>
    </p>

    <script>
        var ext = Vue.extend({
            template: '<p>{{ msg }}</p>',
            data: function(){
                return {
                    msg: '我是扩展的data'
                }
            },
            beforeCreate: function(){
                console.log('1-beforeCreate 创建之前');
            },
            created: function(){
                console.log('2-created 创建之后');
            },
            beforeMount: function(){
                console.log('3-beforeMount 挂载之前');
            },
            mounted: function(){
                console.log('4-mounted 挂载之后');
            },
            beforeUpdate: function(){
                console.log('5-beforeUpdate 数据更新前');
            },
            updated: function(){
                console.log('6-updated 被更新后');
            },
            activated: function(){
                console.log('7-activated');
            },
            deactivated: function(){
                console.log('8-deactivated');
            },
            beforeDestroy: function(){
                console.log('9-beforeDestroy 销毁之前');
            },
            destroyed: function(){
                console.log('10-destroyed 销毁之后')
            }
        });

        let a;

        function mount(){
            a = new ext().$mount('#app'); // 将ext挂载到#app下, a是Vue的实例
        }

        function forceUpdate(){
            if (a.msg !== '我是扩展更新后的data2') {
                a.msg = '我是扩展更新后的data2';
            } else {
                a.msg = '我是扩展更新后的data1';
            }  
        }

        // 当Vue构造器里的data值被修改完成后会调用这个方法，也相当于一个钩子函数吧，和构造器里的updated生命周期很像
        function nextTick(){
            a.msg = "update message info ";
            a.$nextTick(function(){
                console.log('msg更新完后我被调用了');
            })
        }

        function destroy(){
            a.$destroy();
            console.log('被销毁啦')
        }

    </script>
    ```

- 事件
    ```
    <div id="app">
        {{ num }}
        <p><button @click='add'>内部调用内部声明的方法add</button></p>
        <p><button onclick='red()'>内部调用外部声明的方法red</button></p>
    </div>
    <!-- <p><button onclick='red()'>外部调用red</button></p> -->
    <p><button onclick='once()'>外部调用外部声明的方法once</button></p>
    <p><button onclick='off()'>外部调用外部声明的方法off</button></p>

    <script>
        
        var app = new Vue({ // 实例化
            el: '#app', 
            data: {
                num: 1
            }, // 参数
            methods: {
                add: function(){
                    this.num ++;
                }
            }
        });
        
        // 在构造器外部添加事件
        app.$on('red', function(){
            console.log('外部定义的red方法被执行');
            this.num --;
        });
        function red(){
            app.$emit('red') // 外部声明的事件需由实例化对象来emit(发射)
        }

        // 执行一次的事件
        app.$once('redOnce',function(){
            console.log('redOnce被执行');
            this.num --;
        });
        // 
        function once(){
            app.$emit('redOnce')
        }
        // 关闭red事件
        function off(){
            console.log('off被执行');
            app.$off('red')
        }
    </script>
    ```

- 插槽:slot
    ```
    <div id="app">
        <ls>
            <span slot='webSite'>{{inf.webSite}}</span>
            <span slot='webName'>{{inf.webName}}</span>
        </ls>
    </div>
    <template id="inf">
        <div>
            <p>网址是:<slot name='webSite'></slot></p>
            <p>网名是:<slot name='webName'></slot></p>
        </div>
    </template>
    
    <script>
        var ls = {
            template: '#inf'
        };
        var app = new Vue({
            el: '#app',
            data: {
                inf: {
                    webSite: 'http://www.bilibili.com',
                    webName: 'LostStars'
                }
            },
            components: {
                ls: ls
            }
        })
    </script>
    ```