# vue-router 
## [简介](http://jspang.com/post/vue-router.html)
## 环境
- `npm install vue-router --dev-save`开发模式本地模式下安装router

## 文件介绍
- `index.js`
    ```
    import Vue from 'vue'
    import Router from 'vue-router'
    import HelloWorld from '@/components/HelloWorld' // webpack.base.conf.js 文件中定义@解析src目录下的文件

    Vue.use(Router); // 全局使用Router

    export default new Router({
        routes: [
            {
            path: '/',
            name: 'HelloWorld',
            component: HelloWorld
            }
        ]
    })
    ```

## 路由
- 新建一个简单的路由
    - `index.js`
        ```
        export default new Router({
            routes: [
                {
                    path: '/',
                    name: 'HelloWorld',
                    component: HelloWorld
                },{
                    path: '/hi',
                    name: 'hi',
                    component: hi
                }
            ]
        })
        ```
    - `hi.vue`
        ```
        <template>
            <div>
                <h1>{{ msg }}</h1>
            </div>
        </template>

        <script>
            export default {
                name: "hi",
                data(){
                    return {
                        msg: '我是新建的hi路由'
                    }
                }
            }
        </script>

        <style scoped>

        </style>
        ```

- 导航功能
    - `App.vue`
        ```
        <div>
            <router-link to="/">去首页</router-link>
            <router-link to="/hi">去hi页面</router-link>
        </div>
        ```

## 子路由
- 配置子路由
    - `App.vue`
        ```
        <div>
            <router-link to="/">去首页</router-link>
            <router-link to="/hi">去hi页面</router-link>
            <router-link to="/hi/1">去hi-1页面</router-link>
            <router-link to="/hi/2">去hi-2页面</router-link>
        </div>
        ```
    
    - `Hi.vue`
        ```
        <template>
            <div>
                <h1>{{ msg }}</h1>
                <router-view></router-view>
            </div>
        </template>
        ```
    
    - 新建`Hi1.vue`和`Hi2.vue`

    - 配置`index.js`
        ```
        {
            path: '/hi',
            name: 'hi',
            component: hi,
            children: [
                {
                    path: '1',
                    component: hi1
                },{
                    path: '2',
                    component: hi2
                },
            ]
        }
        ```

## 路由的参数传递
- 用name传递参数
    - `App.vue`
        - `{{ $route.name }}`获取当前路由的name信息
        - 改造导航的路径
            ```
            <div>
                <router-link to="/">去首页</router-link>
                <router-link :to="{name: 'hi', params: {user: 'ls'}}">去hi页面</router-link>
                <router-link :to="{name: 'hi1'}">去hi-1页面</router-link>
                <router-link :to="{name: 'hi2'}">去hi-2页面</router-link>
            </div>
            ```
        
    - `Hi.vue`
        - `{{ $route.params.user }}`
- 