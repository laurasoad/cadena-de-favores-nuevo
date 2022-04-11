<template>
  <h1>Publication detail:  {{ publication.id_pub }} </h1>
  <ul class="pub-item">
    <li>Title: {{ publication.title }}</li>
    <li>Type: {{ publication.publication_type }}</li>
    <li>Categories: {{ publication.categories }}</li>
    <li>Date: {{ publication.date }}</li>
    <li>Location: {{ publication.location }}</li>
    <li>Description: {{ publication.description }}</li>
   
  </ul>
</template>
<script>

import config from "@/config.js"; 

export default {
  name: "PublicationDetail", 
  data() {
    return {
      publication: {},
     
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
   
      let publicationId = this.$route.params.id;
      const settings = {
        method: "GET",
        headers: {
        //  JSON application (aun sin user)
        },
      }
     
      const response = await fetch(
        `${config. API_PATH}/publications/${publicationId}`,
        settings);

      this.publication = await response.json();
      },
  },
};
</script>
<style scoped>
h1 {
  font-style: italic;
}
.pub-item {
  list-style: none;
  
  text-align: left;
  padding: 1em;
  border: 2px solid #04AA6D;
  border-radius: 1em;
  margin: 1em;
}


</style>