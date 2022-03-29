<template>
  <h1>Publication detail:  {{ publication.id_pub }} </h1>
  <ul class="publication-item">
    <li>Type: {{ publication.first_name }}</li>
    <li>Title: {{ publication.email }}</li>
    <li>Description: {{ publication.phone }}</li>
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
        `${config. API_PATH}/publications/${contactId}`,
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
.contact-item {
  list-style: none;
  
  text-align: left;
  padding: 1em;
  border: 2px solid dodgerblue;
  border-radius: 1em;
  margin: 1em;
}
</style>