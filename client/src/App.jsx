import { useState, useEffect } from "react"
import vehiclesDatabase from "./services/vehiclesDatabase"

function App() {
  const [vehicles, setVehicles] = useState([])

  useEffect(() => {
    vehiclesDatabase.getAll().then((response) => {
      console.log(response)
      setVehicles(response.data)
    })
  }, [])

  const doesTypeStartWithVowel = (type) => {
    return ["a", "e", "i", "o", "u"].includes(type[0].toLowerCase())
  }

  return (
    <div>
      <h1>Welcome to the template for React + Django + PostgreSQL!</h1>
      <p>Our database has the following vehicles:</p>
      {vehicles.map((vehicle) => (
        <div key={vehicle.id}>
          The <b>{vehicle.name}</b>, which is {doesTypeStartWithVowel(vehicle.type) ? "an" : "a"}{" "}
          <b>{vehicle.type}</b> vehicle. It has{" "}
          <b>{vehicle.numberWheels ? vehicle.numberWheels : "no"}</b> wheels.
        </div>
      ))}
    </div>
  )
}

export default App
