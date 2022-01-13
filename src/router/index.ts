import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import CreateAccount from '@/components/CreateAccount.vue'
import Login from '@/components/Login.vue'
import Dashboard from '@/components/Dashboard.vue'


const routes = [
    {
        path: '/',
        name: "Home",
        component: Home,
        children: [
            {
                path: '/new',
                name: "CreateAccountForm",
                component: CreateAccount
            },
            {
                path: '/',
                name: "Login",
                component: Login
            },
        ]
    },
    {
        path: '/dashboard',
        name: "Dashboard",
        component: Dashboard,
        meta: {
            // requiresAuth: true
        }
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth && !localStorage.token) next({
        path: '/'
    })
    else next()
})


export default router