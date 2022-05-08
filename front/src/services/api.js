import config from "@/config.js";



export async function getPublications() {
    
    const response = await fetch(`${config.API_PATH}/publications`);
    const pub_list = await response.json();
    return pub_list;
  }
  

  export async function addPublication(newPub) {
    const settings = {
        method: "POST",
        body: JSON.stringify(newPub),
        headers: {
          "Content-Type": "application/json",
        },
      }
    await fetch(`${config.API_PATH}/publications`, settings);
  
    }
  
  