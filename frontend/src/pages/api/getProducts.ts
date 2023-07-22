import type { NextApiRequest, NextApiResponse } from "next";
import axios from "axios";

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

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<Product[] | { message: string }>
) {
  const { search } = req.query;
  const url = "http://127.0.0.1:8000/api/endpoints/products";
  try {
    const response = await axios.get(url, {
      params: {
        search: search,
      },
    });
    res.status(200).json(response.data);
  } catch (error: unknown) {
    if (error instanceof Error) {
      res.status(500).json({
        message: error.message,
      });
    } else {
      res.status(500).json({
        message: "An unexpected error occurred.",
      });
    }
  }
}
