<template>
  <h1>Publication detail:  {{ publication.id_pub }} </h1>
  <ul class="pub-item">
    <li>Title: {{ publication.title }}</li>
    <li>Type: {{ publication.publication_type }}</li>
    <li>Description: {{ publication.description }}</li>
    <li>Location: {{ publication.location }}</li>
    <li>Date: {{ publication.date }}</li>
    <li>Categories: {{ publication.categories }}</li>

  </ul>
  <button >
    <router-link :to="`/publications/${publication.id_pub}/edit`">Editar</router-link>
    </button> 
</template>
<script>

import { getPublicationById } from "@/services/api.js";

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
      this.publication = await getPublicationById(publicationId)
      }
      
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