import { Flex, VStack, Text, Link } from "@chakra-ui/react";
interface FooterProps extends FlexProps {}
const Footer: React.FC<FooterProps> = (props) => {
  return (
    <>
      <VStack
        bg="rgba(221, 221, 221, 0.7)"
        p={3}
        borderTop="3px solid rgba(170, 170, 170, 0.3)"
      >
        <Text color="#00010D">
          문의 :{" "}
          <Link href="mailto:siyea0405@gmail.com" isExternal>
            siyea0405@gmail.com
          </Link>
        </Text>
        <Flex direction="column" w="100%" bg="rgba(221, 221, 221, 0.7)">
          <Text
            fontSize="xs"
            color="#666666"
            borderTop="1px solid rgba(170, 170, 170, 0.5)"
          >
            OliveDB는 개인이 만든 취미 프로젝트이며 Oliveyoung과 제휴하지
            않습니다.
          </Text>
          <Text fontSize="xs" color="#666666">
            주기적인 업데이트 후 제품 가격이 변경되므로, OliveYoung의 제품
            가격과 다르게 조회될 수 있습니다.
          </Text>
        </Flex>
      </VStack>
    </>
  );
};

export default Footer;
