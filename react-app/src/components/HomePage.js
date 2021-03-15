import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from "react-redux";
import PokemonCards2 from "./PokemonCards2"
import * as team_actions from '../store/teams'

const HomePage = () => {

    // const [teams, setTeams] = useState()
    const [loaded, setLoaded] = useState(false);

    const dispatch = useDispatch()
    const teams = useSelector((state) => state.teams)

    useEffect(() => {

        dispatch(team_actions.allTeams())
        setLoaded(true)

    }, [dispatch])

    return (
        loaded && (
            <>
                <div>
                    {
                        Object.values(teams).map((team) => <PokemonCards2 key={team.id} team={team}/>)
                    }
                </div>
            </>
        )
    )
}

export default HomePage
