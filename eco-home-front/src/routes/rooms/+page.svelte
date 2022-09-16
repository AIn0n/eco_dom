<script>
	import Header from "../_components/Header.svelte";
  
  
  const url = "http://127.0.0.1:5000";
  let rooms_res;
  let newRoomName = "";
  let msg = "";
  let isNewMsg = false;

  refresh();

  function refresh() {
    rooms_res = fetch(url + "/rooms", { method : "GET"}).then(r => r.json());
  };
  
  
  async function createRoom() {
    const response = fetch(url + "/create_room",
    {
      method : 'POST',
      body: new URLSearchParams({
        "name" : newRoomName
      })
    }).then(r => refresh()).catch(e => {
      msg = e.message;
      isNewMsg = true;
    });
  }
</script>

<Header />
<div class="columns">
    <div class="column is-one-fifth">
      <div class="columns is-1 section">
        <input class="input is-rounded is-small column is-11" type="text" bind:value={newRoomName} placeholder="add new room" required>
        <button class="button is-primary is-small is-rounded column" on:click={createRoom}>+</button>
      </div>
      <aside class="menu">
        <ul class="menu-list">
          {#await rooms_res}
            <progress class="progress is-small is-primary" max="100">15%</progress>
          {:then rooms}
            {#if rooms.length > 0}
              {#each rooms as room}
                <li><a>{room}</a></li>
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
