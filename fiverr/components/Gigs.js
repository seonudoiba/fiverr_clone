import React from "react";
import Gig from "../components/Gig";

export default function Gigs({ lists }) {
  let mylists = lists.products;
  return (
    <div className="grid grid-cols-5 gap-12 m-8">
      {mylists.map((list) => (
        <Gig key={list.id} list={list} />
      ))}
    </div>
  );
}
