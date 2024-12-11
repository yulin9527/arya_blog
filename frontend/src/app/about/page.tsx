"use client";
import { useEffect, useState } from "react";
import Vditor from "vditor";
import "vditor/dist/index.css";

const VditorComponent = () => {
  const [vd, setVd] = useState<Vditor>();

  useEffect(() => {
    const vditor = new Vditor("vditor", {
      after: () => {
        vditor.setValue("");
        setVd(vditor);
      },
    });

    return () => {
      vd?.destroy();
      setVd(undefined);
    };
  }, []);

  const handlePublish = () => {
    if (vd) {
      const content = vd.getValue();
      console.log(content);
    }
  };

  return (
    <div>
      <div id="vditor" className="vditor" />
      <button onClick={handlePublish}>发布</button>
    </div>
  );
};

export default VditorComponent;
