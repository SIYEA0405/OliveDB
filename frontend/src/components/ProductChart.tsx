import { useEffect, useRef } from "react";

interface ProductChartProps {
  data: number[];
  labels: string[];
}

// const ProductCahrt = ({ data, labels }: ProductChartProps) => {
//   const chartContainer = useRef(null);

//   useEffect(() => {
//     if (chartContainer && chartContainer.current) {
//       const newChartInstance = new Chart(chartContainer.current, {
//         type: "line",
//         data: {
//           labels,
//           datasets: [
//             {
//               label: "Sample Data",
//               data,
//             },
//           ],
//         },
//       });

//       return () => {
//         newChartInstance.destroy();
//       };
//     }
//   }, [chartContainer, data, labels]);

//   return <canvas ref={chartContainer} />;
// };

// export default ProductCahrt;
