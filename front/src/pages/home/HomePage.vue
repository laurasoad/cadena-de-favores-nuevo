<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/img/logo.png" />

    <h1>{{ title }}</h1>
    <button  @click="onGoToPublicationsClicked">Go to publication List</button>


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

    },


    onGoToPublicationsClicked() {
      console.log("---> onGoToPublicationsClicked()")

      // this.localUser.id = this.selectedUser.id,
      //this.localUser.name = this.selectedUser.name
      
      // 2) Ir a la pagina de contactos
        this.$root.$forceUpdate();
        this.$router.push("/publications");
      }

  }


}
</script>

<style scoped>
h1 {
  font-style: italic;
}

button {
  border: 2px solid black;
  background-color: white;
  color: black;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  border-color: #04AA6D;
  color: #04AA6D;
 
  text-shadow: 1px #837c7c;
}

button:hover {
  background-color: #04AA6D;
  color: white;
}
</style>
