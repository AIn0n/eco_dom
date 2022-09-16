<script>
	import Header from "../_components/Header.svelte";
  
  
  const url = "http://127.0.0.1:5000";
  let rooms_res;
  let devices_res;
  let newRoomName = "";
  let msg = "";
  let isNewMsg = false;

  rooms_refresh();

  function rooms_refresh() {
    rooms_res = fetch(url + "/rooms", { method : "GET"}).then(r => r.json());
  };

  function get_devices(id) {
    devices_res = fetch(url + "/rooms/" + id + "/devices");
  }  
  
  async function createRoom() {
    const response = fetch(url + "/create_room",
    {
      method : 'POST',
      body: new URLSearchParams({
        "name" : newRoomName
      })})
    .then(r => {if (r.status == 200) { 
      rooms_refresh(); };})
      .catch(e => {
        msg = e.message;
        isNewMsg = true;
      });
  }
</script>

<Header />
<div class="columns">
    <div class="column is-one-fifth has-background-light">
      <div class="columns is-1 section">
        <input class="input is-rounded is-small column is-11" type="text" bind:value={newRoomName} placeholder="add new room" required>
        <button class="button is-primary is-rounded is-small column" on:click={createRoom}>add</button>
      </div>
      <aside class="menu">
        <ul class="menu-list">
          {#await rooms_res}
            <progress class="progress is-small is-primary" max="100">15%</progress>
          {:then rooms}
            {#if rooms.length > 0}
              {#each rooms as room}
                <li><button class="button is-primary is-rounded is-info is-fullwidth" on:click={get_devices(room["id"])}>{room["name"]}</button></li>
              {/each}
            {:else}
            <li>
              <a>There are no rooms available!</a>
            </li>
            {/if}
          {/await}
        </ul>
      </aside>
    
    </div>
    
    <div class="column">
    
      <div class="block">
        This text is within a <strong>block</strong>.
      </div>
      <div class="block">
        This text is within a <strong>second block</strong>. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Aenean efficitur sit amet massa fringilla egestas. Nullam condimentum luctus turpis.
      </div>
      <div class="block">
        This text is within a <strong>third block</strong>. This block has no margin at the bottom.
      </div>
    </div>
</div>
