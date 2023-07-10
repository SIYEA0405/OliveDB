import type { NextApiRequest, NextApiResponse } from "next";

type Product = {
  _id: string;
  brand: string;
  large_ctg: string;
  name: string;
  price: {
    current: number;
    lowest: number;
    original: number;
  };
  small_ctg: string[];
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Product[]>
) {
  res.status(200).json([
    {
      _id: "64abfffed7e3280256adfbc3",
      brand: "라운드랩",
      large_ctg: "스킨케어",
      name: "라운드랩 1025 독도 토너 500ml+200ml 기획(+소나무 클렌저 10ml 증정)",
      price: {
        current: 29300,
        lowest: 29300,
        original: 45000,
      },
      small_ctg: ["토너/로션/올인원"],
    },
  ]);
}
