const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            goals: ['test1', 'test2'],
            enteredValue: '',
        };
    },
    methods: {
        addGoal() {
            this.goals.push('test');
            test = this.goals
            console.log(test)
        },
    },
});

app.mount('#app');
