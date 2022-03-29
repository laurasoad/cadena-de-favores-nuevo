<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/img/logo.png" />
    <h1>{{ title }}</h1>
    <h2>{{ publication_list }}</h2>
    <button>Go to publication List</button>


  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      title: "Welcome",
      publication_list: []
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/publications')
      this.publication_list = await response.json()


    }
  }


}
</script>

<style scoped>
h1 {
  font-style: italic;
}
</style>
