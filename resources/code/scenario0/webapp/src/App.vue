<template>
    <div id="app" style="background-image: url('./assets/AWS_logo_RGB_WHT.png')">
        <img alt="AWS logo" src="./assets/logo.png">
        <HelloWorld msg="Welcome to the AWS Workshop!"/>

        <div id="api1" >
          <div >
            <button v-on:click="clearCacheUsers()" class="button buttonCache"><h3> Clear Users API redis cache </h3></button>
          </div>
          <p></p>

          <button v-on:click="getUsers()" class="button buttonApi"><h3> Call Users API </h3></button>
            <div v-if="!Object.keys( users ).length == 0">
                <h3>
                    <vue-json-pretty :data="{ users }"> </vue-json-pretty>
                </h3>
            </div>
        </div>

        <div id="api2">
          <div >
            <button v-on:click="clearCachePosts()" class="button buttonCache"><h3> Clear Posts API redis cache </h3></button>
          </div>
          <p></p>

            <button v-on:click="getPosts()" class="button buttonApi"> <h3> Call Posts API </h3></button>
            <div v-if="!Object.keys( posts ).length == 0">
                <h3>
                    <vue-json-pretty :data="{ posts }"> </vue-json-pretty>
                </h3>
            </div>
        </div>

        <div id="api3">

          <div >
            <button v-on:click="clearCacheThreads()" class="button buttonCache"><h3> Clear Threads API redis cache </h3></button>
          </div>
          <p></p>

            <button v-on:click="getThreads()" class="button buttonApi"> <h3> Call Threads API </h3></button>
            <div v-if="!Object.keys( threads ).length == 0">
                <h3>
                    <vue-json-pretty :data="{ threads }"> </vue-json-pretty>
                </h3>
            </div>
        </div>


    </div>
</template>

<script>
    import HelloWorld from './components/HelloWorld.vue'
    import axios from "axios";
    import VueJsonPretty from 'vue-json-pretty';
    import 'vue-json-pretty/lib/styles.css';

    export default {
        name: 'App',
        components: {
            HelloWorld,
            VueJsonPretty
        },

        data() {
            return {
                users: {},
                posts: {},
                threads: {},
                url: process.env.VUE_APP_API_URL
            };
        },

        methods: {

            async getUsers() {
                const path = this.url + "/api/users";
                axios.get(path).then(
                    (response) => {
                        this.users = response.data;
                        console.log(response.data);
                    },
                    (error) => {
                        console.log(error);
                    }
                );
            },

            async getPosts() {
                const path = this.url + "/api/posts";
                axios.get(path).then(
                    (response) => {
                        this.posts = response.data;
                        console.log(response.data);
                    },
                    (error) => {
                        console.log(error);
                    }
                );
            },

            async getThreads() {
                const path = this.url + "/api/threads";
                axios.get(path).then(
                    (response) => {
                        this.threads = response.data;
                        console.log(response.data);
                    },
                    (error) => {
                        console.log(error);
                    }
                );
            },

          async clearCacheUsers() {
            const path = this.url + "/api/users/clear-cache";
            axios.get(path).then(
                (response) => {
                  this.users = {};
                  console.log(response.data);
                },
                (error) => {
                  console.log(error);
                }
            );
          },

          async clearCachePosts() {
            const path = this.url + "/api/posts/clear-cache";
            axios.get(path).then(
                (response) => {
                  this.posts = {};
                  console.log(response.data);
                },
                (error) => {
                  console.log(error);
                }
            );
          },

          async clearCacheThreads() {
            const path = this.url + "/api/threads/clear-cache";
            axios.get(path).then(
                (response) => {
                  this.threads = {};
                  console.log(response.data);
                },
                (error) => {
                  console.log(error);
                }
            );
          },

        },

        pretty: function(value) {
            return JSON.stringify(JSON.parse(value), null, 2);
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }

    #api1, #api2, #api3 {
        display: inline-block;
        width: 500px;
        float: left;
    }

    .button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }

    .buttonCache {
        width: 250px;
        background-color: lightslategrey;
    }
    .buttonApi {width: 250px;}

    textarea {
        width: 100%;
        min-height: 30rem;
        font-family: "Lucida Console", Monaco, monospace;
        font-size: 0.8rem;
        line-height: 1.2;
    }

</style>
