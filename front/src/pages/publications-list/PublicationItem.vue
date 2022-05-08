<template>
   <article class="pub-item">
      <p>Title: {{ publication.title }}</p>
      <p>Type: {{ publication.publication_type }}</p>
      <p> Categories: {{ publication.categories }}</p>
      <p>Location: {{ publication.location }}</p>
      <button>
         <router-link :to="`/publications/${publication.id_pub}`">Details</router-link>
      </button>
   </article>
</template>

<script>
export default {
  name: "PublicationItem",
  props: {
    publication: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>


  .pub-item {
    flex: 1 1 21rem;
    border: 2px solid #04AA6D;
    border-radius: 1em;
    margin: 1em 2em;
    padding: 1em 2em;
    /*max-width: 10em;*/
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-self: normal;


  }

  .pub-item:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

  button {
  border: 2px solid #04AA6D;
  background-color: white;
  color: black;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  background-color: #04AA6D;
  color: white;
  
  text-shadow: 1px #837c7c;
  border-radius: 0.5em;
}

button:hover {
  color: #04AA6D;
  background-color: white;
  border-color: #04AA6D;

  
}
a:link, a:visited, a:active {
    text-decoration:none;
      color:#2c3e50
}

</style>
