import React from "react";
import { Link } from "react-router-dom";
import { TypeAnimation } from "react-type-animation";

const Hero = () => {
  return (
    <div className="text-white">
      <div className="pt-20 max-w-[800px] mt-[-96px] w-full h-screen mx-auto text-center flex flex-col justify-center">
        <p className="text-[#00df9a] md:text-3xl sm:text-3xl text-xl font-bold p-2">
          GROWING WITH UNI
        </p>
        <h1 className="md:text-7xl sm:text-6xl text-4xl font-bold md:py-3">
          Grow with SASI
        </h1>
        <div className="flex justify-center items-center">
          <TypeAnimation
            className="md:text-6xl sm:text-5xl text-4xl italic font-mono font-bold md:pl-4 pl-2 pt-3"
            sequence={[
              "Student",
              1000,
              "Academic",
              1000,
              "Support",
              1000,
              "Intelligence",
              1000,
            ]}
            speed={1}
            repeat={Infinity}
          />
        </div>
        <p className="md:text-2xl text-xl font-bold text-gray-500 pt-2">
          Your intelligent AI-powered academic support companion at your
          service.
        </p>
        <Link to="/chat" className=" cursor-default">
          <button className="bg-[#00df9a] w-[200px] rounded-md font-medium my-6 mx-auto py-3 text-black">
            Get Started
          </button>
        </Link>
      </div>
    </div>
  );
};

export default Hero;
